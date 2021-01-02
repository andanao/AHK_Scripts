import numpy
import webbrowser
import svgwrite
from svgwrite import cm, mm, inch
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

class paper_maker:
    def __init__(self,name, pg_corners = False, ):
        self.dwg = svgwrite.Drawing(
            filename=name,
            size = (u'11in',u'8.5in')
            # debug=True,
            # profile='full',
            # height = '8.5in',
            # width='11in'
            )
        pg_corners = [0,0,11,8.5]
        margins = [
            1*cm, # Left
            1*cm, # Right
            1*cm, # Top
            1*cm  # Bottom
            ]


    def note_paper(self): #
        pg_corners = [0,0,11,8.5]
        margins = [
            1.5, # Left
            1, # Right
            1.5, # Top
            1  # Bottom
            ]
        for i in range(len(margins)):
            margins[i] = margins[i]/2.54


        corners_1 = [
            0+margins[0],   #x1
            0+margins[2],    #y1
            pg_corners[2]/2-margins[1],#x2
            pg_corners[3]-margins[3]   #y2
            ]
        corners_2 = [
            pg_corners[2]/2+margins[0],
            0+margins[2],
            pg_corners[2]-margins[1],
            pg_corners[3]-margins[3]
            ]

        
        # self.pg_outline(pg_corners,True)
        self.h_lines(corners_1,35)
        self.h_lines(corners_2,35)
        
        self.dwg.add(self.dwg.rect(
            insert = ((corners_1[2]-.1)*inch,(.3)*inch),
            size = (.1*inch,.1*inch),
            stroke = 'black',
            stroke_opacity = '.5',
            stroke_width = '.5',
            fill_opacity = '0'
        ))
        self.dwg.add(self.dwg.rect(
            insert = ((corners_2[2]-.1)*inch,(.3)*inch),
            size = (.1*inch,.1*inch),
            stroke = 'black',
            stroke_opacity = '.5',
            stroke_width = '.5',
            fill_opacity = '0'
        ))

        self.save_dwg()

    def save_dwg(self):
        self.dwg.save(pretty=True)
        print('Drawing Saved')

    def pg_outline(self, pg_corners,half=False):
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
        if half:
            olines.add(self.dwg.line(
                start=(pg_corners[2]/2*inch, pg_corners[3]*inch), 
                end=(pg_corners[2]/2*inch, pg_corners[0]*inch)
                ))
        
        # return olines

    def h_lines(self,corners,count):
        hlines = self.dwg.add(self.dwg.g(id='hlines',
            stroke='#000000',
            stroke_width = '.5',
            stroke_opacity = '.5',
            stroke_dasharray='.5 2.75',
            stroke_linecap="round"
        ))
        # linenote = self.dwg.add(self.dwg.g(id='linenote',
        #     stroke='#000000',
        #     # stroke_width = '.5',
        #     # stroke_opacity = '1',
        #     # stroke_dasharray='.5 10',
        #     # stroke_linecap="round"
        # ))
        
        spacing = abs(corners[3]-corners[1])/count
        # for i in range(count):
        for i in range(count+1):
            # dasharray = '.5 '+ str(round(i/35*20,2))
            hlines.add(self.dwg.line(
            start=(corners[0]*inch, (corners[1]+spacing*i)*inch), 
            end=(corners[2]*inch, (corners[1]+spacing*i)*inch),
            # stroke_dasharray=dasharray
            ))
            # linenote.add(
            #     self.dwg.text(
            #         dasharray,
            #         insert = (corners[0]*inch, (corners[1]+spacing*i)*inch),
            #         font_size='10'
            #         )
            # )
    # def lines(dw)

if __name__ == '__main__':
    name = 'note_paper_01_front'
    # name = 'note_paper_01_back'
    namesvg = name+'.svg'
    namepdf = name+'.pdf'
    maker = paper_maker(namesvg)
    maker.note_paper()
    webbrowser.open(namesvg)


    drawing = svg2rlg(namesvg)
    renderPDF.drawToFile(drawing,namepdf)
    # webbrowser.open(namepdf)
    # chrome_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s'
    # chrome_path ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    # webbrowser.get(chrome_path).open(namepdf)
