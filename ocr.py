import easyocr
import datetime

class ocr:

    def image_to_text():
     try:

        reader = easyocr.Reader(['en'])

        # result = reader.readtext("crop/crop.jpg",paragraph="False")
        result = reader.readtext("crop4.jpg",paragraph="True")
        print(result[0][1])
        # Write-Overwrites
        file1 = open("ocr.txt","w")#write mode
        file1.write(f"{result[0][1]} \n")
        file1.close()
        return result[0][1]
     
     except Exception as e:
         print(e)



