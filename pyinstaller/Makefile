.PHONY: setup build clean zipapp release

setup:
	poetry install

build: setup
	poetry run pyinstaller trainscanner.spec

clean:
	rm -rf dist build
	rm -f *.spec

# trainscannerのバージョンをpyproject.tomlから取得
VERSION := $(shell poetry show trainscanner | awk '/version/ {print $$3}')
APP_NAME := trainscanner-$(VERSION)-arm64.app
ZIP_NAME := $(APP_NAME).zip

$(ZIP_NAME):
	cd dist && zip -r ../$(ZIP_NAME) $(APP_NAME)

release: $(ZIP_NAME)
	gh release create v$(VERSION) $(ZIP_NAME) --title "TrainScanner v$(VERSION) (Apple Silicon)" --notes "Apple Silicon (arm64) 用 .app バンドルです。" 