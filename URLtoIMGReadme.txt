There are comments in urltoimg.py that note important ines, but I'm also describing the process in this readme
1. use the line: 'from io import BytesIO' io is included in python, so you don't need to install a new module
2. After fetching the API data, find the URL for the image you want and save it
3. once you have the URL, read it into pillow by uding the line: img = Image.open(BytesIO(url.content)) where url is whatever contains the image URL
4. Thats it! you should have the API image saved as an img, which you can then use in image manipulations