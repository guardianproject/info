all: website

userconfig.yaml:
	touch userconfig.yaml

website: pre-serve userconfig.yaml gnupg-web-key-directory
	./setup-fdroid-data.py
	./setup-pages-for-supported-languages.py
	awk '{if(/^[a-z]/){k=$$0;gsub("[ \t]*=.*$$","",k);if(!(k in A)){A[k]=$$0;print}}else{print}}' \
		userconfig.yaml config.yaml > gitlab.yaml
	hugo --config gitlab.yaml 

serve: pre-serve
	hugo server --i18n-warnings

pre-serve:
	mkdir data > /dev/null 2> /dev/null; true
	mkdir content > /dev/null 2> /dev/null; true
	echo "describe: \"$$( git describe --always )\"" > data/git.yaml
	echo "hash: \"$$( git rev-list HEAD --max-count=1 )\"" >> data/git.yaml
	echo "project: \"$$( basename $$PWD )\"" >> data/git.yaml
	echo "commitDate: \"$$( git log -n 1 --pretty=format:%ci )\"" >> data/git.yaml

wkd = public/.well-known/openpgpkey
keyids := $(shell grep -Eo '^ *gpg: *[A-Fa-f0-9]{40}.*' data/teamlist.yaml | awk '{print $$2}')
gnupg-web-key-directory:
	gpg --import team-keyring.gpg
	for keyid in $(keyids); do gpg --keyserver keys.openpgp.org --recv-keys $$keyid; done
	test -d $(wkd) || mkdir -p $(wkd)
	touch $(wkd)/policy
	cd $(wkd)/.. && for keyid in $(keyids); do \
		gpg --list-options show-only-fpr-mbox --list-public-keys $$keyid \
			| /usr/lib/gnupg/gpg-wks-client -v --install-key; \
	done

clean:
	rm -f \
		data/git.yaml \
		gitlab.yaml userconfig.yaml
	rm -rf	public

# Remove everything, even things that need to be redownloaded
distclean: clean

.PHONY: all website serve pre-serve clean distclean
