from random import randint
import webbrowser

president = {1:'George Washington', 2:'John Adams', 3:'Thomas Jefferson', 4:'James Madison', 5:'James Monroe', 6:'John Quincy Adams', 7:'Andrew Jackson', 8:'Martin Van Buren', 9:'William Henry Harrison', 10:'John Tyler', 11:'James Knox Polk',
	12:'Zachary Taylor', 13:'Millard Fillmore', 14:'Franklin Pierce', 15:'James Buchanan', 16:'Abraham Lincoln', 17:'Andrew Johnson', 18:'Ulysses Grant', 19:'Rutherford Birchard Hayes', 20:'James Abram Garfield', 21:'Chester Alan Arthur', 22:'Grover Cleveland',
	23:'Benjamin Harrison', 24:'William McKinley', 25:'Theodore Roosevelt', 26:'William Howard Taft', 27:'Woodrow Wilson', 28:'Warren Gamaliel Harding', 29:'Calvin Coolidge', 30:'Herbert Hoover', 31:'Franklin Delano Roosevelt', 32:'Harry Truman', 33:'Dwight David Eisenhower',
	34:'John Fitzgerald Kennedy', 35:'Lyndon Baines Johnson', 36:'Richard Nixon', 37:'Gerald Ford', 38:'Jimmy Carter', 39:'Ronald Reagan', 40:'George Herbert Walker Bush', 41:'Bill Clinton', 42:'George Walker Bush', 43:'Barack Obama'}

select = randint(1,43)

sepName = president[select].split()

if len(sepName) == 2:
	url = "https://en.wikipedia.org/wiki/" + sepName[0] + "_" + sepName[1]
	
elif len(sepName) == 3:
	url = "https://en.wikipedia.org/wiki/" + sepName[0] + "_" + sepName[1] + "_" + sepName[2]
	

webbrowser.open(url, new=1)
