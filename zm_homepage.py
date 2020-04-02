#Filename zm_homepage.py
#主页部分
def get_homepage():
    head='<!doctype html><html lang="en-US"><head><meta http-equiv="content-type" content="text/html; charset=utf-8"><title>DOLLARS</title><link href="app.css" rel="stylesheet"></head>'
    body='<body><div id="body"><div class="home-wrap"><div class="login-logo"></div><form action="" method="post" name="myform"><div class="login-form field" id="t_form"><div class="home-name"><label for="form-name">USERNAME:</label><input type="text" id="form-name" name="name" size="10" maxlength="20" class="home-name-input" required autocomplete="on"></div><div class="home-submit"><input type="submit" name="login" value="ENTER" class="submit-input home-submit-input"></div></div></form></div></div></body></html>'
    return head+body