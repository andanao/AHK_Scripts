# %%
import re

def clean_notes(input_f = "notes_raw.txt",to_file= False, out_f='notes_cleaned.txt'):
    file = open(input_f, "r",encoding='utf-8').read()

    cleaned_text = re.sub(r'(?<=[\u4e00-\u9fff])\d','',file) # remove numbers between 汉字
    cleaned_text = re.sub(r'[【\[].*[】\]]','',cleaned_text) #remove stuff between brackets
    # print('hi')
    cleaned_text = re.sub(r'.*\:.*','',cleaned_text)
    cleaned_text = re.sub(r'.*\ds.*','',cleaned_text)
    cleaned_text = re.sub(r'\/','\n',cleaned_text)
    cleaned_text = re.sub(r'(早上好|你好)','',cleaned_text)#remove good morning and stuff
    cleaned_text = re.sub(r'[^\u4e00-\u9fff]{2,}','\n',cleaned_text)

    if to_file:
        f = open(out_f, "w+",encoding='utf-8')
        f.write(cleaned_text)
        f.close()
    else:
        print("\n\t{} cleaned input file, output to file supressed".format(input_f))
    return cleaned_text


if __name__ == "__main__":
    clean_notes(to_file=True)

    # if click.confirm('Check cleaned.txt for logic',default=True):
    # make_anki()
#
# %%
