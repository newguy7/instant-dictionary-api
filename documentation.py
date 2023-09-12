import justpy as jp


class Doc:
    
    def serve(self):
        wp = jp.WebPage()        

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definitions of words:", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=circle")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "circle", "definition": ["A two-dimensional, geometric shape that is made up of every point on a plane which is equidistant from the centre. 
        May be drawn with a pair of compasses.", "Group of persons who have common ideas, interests or occupations.", "To move in circles."]}
        """)
        return wp
