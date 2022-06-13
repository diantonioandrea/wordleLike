compile:
	pyinstaller -F src/wordleLike.py
	if [ ! -d "wordlePack" ]; then mkdir wordlePack; fi
	mv dist/* wordlePack/
	cp words/words.txt wordlePack/

clean:
	rm -rf dist build __pycache__
	rm -rf src/__pycache__
	rm *.spec