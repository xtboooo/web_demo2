from django.shortcuts import render, HttpResponse


def register(request):
    """注册 View 视图函数"""
    html = """
    <html>
        <head>
            <title>注册页面</title>
        </head>
        <body>
            <form method='post' action='/register/'>
                username：<input type='text' name='username' /><br/>
                password：<input type='password' name='password' /><br/>
                <input type='submit' value='注册' />
            </form>
        </body>
    </html>
    """
    return HttpResponse(html)
