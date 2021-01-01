import numpy
import webbrowser
import svgwrite
from svgwrite import cm, mm, inch  

class paper_maker:
    def __init__(self,name):
        self.dwg = svgwrite.Drawing(filename=name, debug=True)

    def note_paper(self):

        lmarg = 1*cm
        rmarg = 1*cm
        tmarg = 1*cm
        bmarg = 1*cm

        pg_corners = [0,0,11,8.5]
        self.pg_outline(pg_corners)
        # dwg.add(outlines)


        # hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
        # for y in range(10):
        #     hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
        





        self.dwg.save()


    def pg_outline(self, pg_corners):
        olines = self.dwg.add(self.dwg.g(id='olines',
            stroke='black',
            stroke_width = '1',
            stroke_dasharray='2 5',
            stroke_linejoin="round"
        ))
        olines.add(self.dwg.line(
            start=(pg_corners[0]*inch, pg_corners[0]*inch), 
            end=(pg_corners[2]*inch, pg_corners[0]*inch)
            ))
        olines.add(self.dwg.line(
            start=(pg_corners[2]*inch, pg_corners[0]*inch), 
            end=(pg_corners[2]*inch, pg_corners[3]*inch)
            ))
        olines.add(self.dwg.line(
            start=(pg_corners[2]*inch, pg_corners[3]*inch), 
            end=(pg_corners[0]*inch, pg_corners[3]*inch)
            ))
        olines.add(self.dwg.line(
            start=(pg_corners[0]*inch, pg_corners[3]*inch), 
            end=(pg_corners[0]*inch, pg_corners[0]*inch)
            ))
        olines.add(self.dwg.line(
            start=(pg_corners[2]/2*inch, pg_corners[3]*inch), 
            end=(pg_corners[2]/2*inch, pg_corners[0]*inch)
            ))
        
        # return olines

    # def lines(dw)

if __name__ == '__main__':
    name = 'note_paper_01.svg'
    maker = paper_maker(name)
    maker.note_paper()

    # note_paper('note_paper.svg')
    webbrowser.open(name)

