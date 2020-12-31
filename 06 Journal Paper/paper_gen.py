import numpy
import webbrowser
import svgwrite
from svgwrite import cm, mm, inch  

def note_paper(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)

    lmarg = 1*cm
    rmarg = 1*cm
    tmarg = 1*cm
    bmarg = 1*cm

    pg_corners = [0,0,11,8.5]
    outlines = pg_outline(dwg,pg_corners)
    dwg.add(outlines)


    # hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    # for y in range(10):
    #     hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
    





    dwg.save()


def pg_outline(drawing, pg_corners):
    olines = dwg.add(dwg.g(id='olines',
        stroke='black',
        stroke_width = '1',
        stroke_dasharray='2 5',
        stroke_linejoin="round"
    ))
    olines.add(dwg.line(
        start=(pg_corners[0]*inch, pg_corners[0]*inch), 
        end=(pg_corners[2]*inch, pg_corners[0]*inch)
        ))
    olines.add(dwg.line(
        start=(pg_corners[2]*inch, pg_corners[0]*inch), 
        end=(pg_corners[2]*inch, pg_corners[3]*inch)
        ))
    olines.add(dwg.line(
        start=(pg_corners[2]*inch, pg_corners[3]*inch), 
        end=(pg_corners[0]*inch, pg_corners[3]*inch)
        ))
    olines.add(dwg.line(
        start=(pg_corners[0]*inch, pg_corners[3]*inch), 
        end=(pg_corners[0]*inch, pg_corners[0]*inch)
        ))
    olines.add(dwg.line(
        start=(pg_corners[2]/2*inch, pg_corners[3]*inch), 
        end=(pg_corners[2]/2*inch, pg_corners[0]*inch)
        ))
    
    return olines

if __name__ == '__main__':
    note_paper('note_paper.svg')
    webbrowser.open('note_paper.svg')
# basic_shapes('note_paper.svg')

# open('note_paper.svg')
