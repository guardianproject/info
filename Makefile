all: website

userconfig.yaml:
	touch userconfig.yaml

website: pre-serve userconfig.yaml gnupg-web-key-directory
	./setup-fdroid-data.py
	./setup-pages-for-supported-languages.py
	awk '{if(/^[a-z]/){k=$$0;gsub("[ \t]*=.*$$","",k);if(!(k in A)){A[k]=$$0;print}}else{print}}' \
		userconfig.yaml config.yaml > gitlab.yaml
	hugo --config gitlab.yaml --i18n-warnings

serve: pre-serve
	hugo server --i18n-warnings

pre-serve:
	mkdir data > /dev/null 2> /dev/null; true
	mkdir content > /dev/null 2> /dev/null; true
	echo "describe: \"$$( git describe --always )\"" > data/git.yaml
	echo "hash: \"$$( git rev-list HEAD --max-count=1 )\"" >> data/git.yaml
	echo "project: \"$$( basename $$PWD )\"" >> data/git.yaml
	echo "commitDate: \"$$( git log -n 1 --pretty=format:%ci )\"" >> data/git.yaml

wkd = public/.well-known/openpgpkey/hu
gnupg-web-key-directory:
	test -d $(wkd) || mkdir -p $(wkd)
	@echo abel@guardianproject.info
	curl --silent https://keys.openpgp.org/vks/v1/by-fingerprint/9185813DDCCD789E5D4BA51B884B649C340C81F4 \
	     > $(wkd)/rhgcizkjn7c9cfr7xttwjrdz1n3t75rt
	@echo hans@guardianproject.info
	curl --silent https://keys.openpgp.org/vks/v1/by-fingerprint/EE6620C7136B0D2C456C0A4DE9E28DEA00AA5556 \
	     > $(wkd)/tyyfxn4t6ytctsfpzfogin37su9pzssg
	@echo harlo@guardianproject.info
	curl --silent https://keys.openpgp.org/vks/v1/by-fingerprint/60FB69097B2A759811A86E0E67866BECA4469630 \
	     > $(wkd)/ddtqgbus58yfcucs7bjd4u74npyckuxi
	@echo nathan@guardianproject.info
	curl --silent https://keys.openpgp.org/vks/v1/by-fingerprint/BBE20FD6DA48A3DD4CC7DF41A801183E69B37AA9 \
	     > $(wkd)/f4fk1gdgyoeakzdpeuk5smpgq6iygc1i
	@echo michael@guardianproject.info
	curl --silent https://keys.openpgp.org/vks/v1/by-fingerprint/3DBDBA23810AEE377CC8E9D7C84324635610899F \
	     > $(wkd)/n6h6dt1ftdd9w3y3sujj5oxwejt8uqob

clean:
	rm -f \
		data/git.yaml \
		gitlab.yaml userconfig.yaml
	rm -rf	public

# Remove everything, even things that need to be redownloaded
distclean: clean

.PHONY: all website serve pre-serve clean distclean
