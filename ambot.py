import webbrowser

def open_website(url):
    webbrowser.open(url)
    import webbrowser

def open_website(url):
    html_code = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>LOVE ❤️</title>
        <style>
            body {{
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            
            h1 {{
                color: #333333;
                text-align: center;
            }}
            
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Website</h1>
            <p>This is a sample website created using Python.</p>
            <p>Feel free to modify and style it as needed!</p><marquee behavior="" direction="right"><h1 align="left">❤️ HAPPY 9MONTHS OF LOVE LOLOVES ❤️ </h1></marquee>
    <div style="text-align: center; border: 2px solid rgb(252, 3, 3); padding: 10px;font-family: Arial, sans-serif; font-size: 16px; color: #e90808;">
        <p>
            HI LOVE, HAPPY 1YR AND 9MONTHS OF LOVE MY LOVE ❤️.
        <br>
            SO THANKFUL TO HAVE YOU IN MY LIFE. THANK YOU FOR BEING AN UNDERSTANDING PARTNER LOVE, SALAMAT KAY MISKI MAKAPUNO NAG BATASAN IMONG UYAB, 
        <br>    
            GINASABOT JAPUN NIMO AKONG PAGKA MALDITA. PAGKA SWERTI BA LAMANG NAKO NATUNONG KOS IMO MISKI BADLUNGON SAHAY HAHHAHA. 
        <br>    
            UNTA MAGDUGAY PATAG AYO LOVE DNANAKO MA IMAGINE AKONG FUTURE NGA WALA KA ILOVEYOU PERMI OVIN NAKO, MWAAAAH MWAAAAH MWAAAH! HAPPY MONTHSARY LOLOVES!
        <br>
            WAKOY MA REGALO NIMO KAY POBRE IMONG UYAB, MISKI MAN LANG KANI MALIPAY KA SLIGHT HAHAHHA! ILOVEYOU MWAAAH MWAAAH MWAAAH!❤️
        </p>
        </div>
    </body>
    </html>
    '''

    with open('website.html', 'w') as file:
        file.write(html_code)

    webbrowser.open('website.html')

# Example usage
open_website('https://loveeee.com')
# Example usage
open_website('https://loveeee.com')
