BUILD=build
SRC=src

$(shell mkdir -p $(BUILD))

all: \
    $(BUILD)/bootstrap \
    $(BUILD)/index.html \
    $(BUILD)/toltec.css \
    $(BUILD)/logo.png \
    $(BUILD)/nao.png
	rm -f $(BUILD)/defs.rst

clean:
	rm -r $(BUILD)

.PHONY: all clean

$(BUILD)/bootstrap:
	wget --no-verbose --output-document "$@" https://raw.githubusercontent.com/toltec-dev/toltec/stable/scripts/bootstrap/bootstrap
	chmod u+x "$@"

$(BUILD)/defs.rst: $(BUILD)/bootstrap
	echo ".. |bootstrap-hash| replace:: $$(sha256sum $^ | cut -b-64)" > "$@"

$(BUILD)/%.rst: $(SRC)/%.rst
	cp "$^" "$@"

$(BUILD)/%.html: $(BUILD)/%.rst $(BUILD)/defs.rst
	rst2html5 --input-encoding utf-8 --output-encoding utf-8 "$<" "$@"

$(BUILD)/%.png: $(SRC)/%.png
	cp "$^" "$@"

$(BUILD)/%.css: $(SRC)/%.css
	cp "$^" "$@"
