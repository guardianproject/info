all: website

userconfig.toml:
	touch userconfig.toml

website: pre-serve userconfig.toml
	awk '{if(/^[a-z]/){k=$$0;gsub("[ \t]*=.*$$","",k);if(!(k in A)){A[k]=$$0;print}}else{print}}' \
		userconfig.toml config.toml > gitlab.toml
	hugo --config gitlab.toml --i18n-warnings

serve: pre-serve
	hugo server --i18n-warnings

pre-serve:
	echo "describe: \"$$( git describe --always )\"" > data/git.yaml
	echo "hash: \"$$( git rev-list HEAD --max-count=1 )\"" >> data/git.yaml
	echo "project: \"$$( basename $$PWD )\"" >> data/git.yaml
	echo "commitDate: \"$$( git log -n 1 --pretty=format:%ci )\"" >> data/git.yaml

clean:
	rm -f \
		data/git.yaml \
		gitlab.toml userconfig.toml
	rm -rf	public

# Remove everything, even things that need to be redownloaded
distclean: clean

.PHONY: all website serve pre-serve clean distclean
