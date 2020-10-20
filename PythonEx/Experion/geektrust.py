#Kindom details
Space=  '{ "name":"SPACE", "emplem":"GORILLA"}'
Land=  '{ "name":"LAND", "emplem":"PANDA"}'
Water=  '{ "name":"WATER", "emplem":"OCTOPUS"}'
Ice=  '{ "name":"ICE", "emplem":"MAMMOTH"}'
Air=  '{ "name":"AIR", "emplem":"OWL"}'
Fire=  '{ "name":"FIRE", "emplem":"DRAGON"}'

#Kindom Name result
kindomList = ['SPACE']

#Cipercode Encrypt
def encrypt(text,s):
    result =""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()): result += (chr((ord(char) + s-65) % 26 + 65))  
        else: result += chr((ord(char) + s - 97) % 26 + 97)             
    return result

#Cipercode Encrypt
def CheckDecryptText(text,emplem):
    result = False
    for i in emplem:
        countLetEmp=emplem.count(i)
        countLetTex=text.count(i)
        if(countLetTex>=countLetEmp):result = True
        else:result =False;break
                     
    return result

#Check Decript Value with emplom
def DecriptTextWithEmplem(fileContentLineKingdom,fileContentLineKingdomMsg):
    
    decryptText=""
    kindomText="" 

    
    if fileContentLineKingdom=="SPACE": 
        decryptText=(encrypt(fileContentLineKingdomMsg,-7))    
        kindomText=(CheckDecryptText(decryptText,"GORILLA"))
    
    if fileContentLineKingdom=="AIR": 
        decryptText=(encrypt(fileContentLineKingdomMsg,-3))       
        kindomText=(CheckDecryptText(decryptText,"OWL"))
        
    if fileContentLineKingdom=="LAND": 
        decryptText=(encrypt(fileContentLineKingdomMsg,-5)) 
        kindomText=(CheckDecryptText(decryptText,"PANDA"))  

    if fileContentLineKingdom=="WATER": 
        decryptText=(encrypt(fileContentLineKingdomMsg,-7)) 
        kindomText=(CheckDecryptText(decryptText,"OCTOPUS"))    

    if fileContentLineKingdom=="ICE": 
        decryptText=(encrypt(fileContentLineKingdomMsg,-7))    
        kindomText=(CheckDecryptText(decryptText,"MAMMOTH"))

    if fileContentLineKingdom=="FIRE": 
        decryptText=(encrypt(fileContentLineKingdomMsg,-6))    
        kindomText=(CheckDecryptText(decryptText,"DRAGON"))

    return kindomText

def AddKindomToList( result, kindomName):
    if(result==True):kindomList.append(kindomName)
  
def main():
       
    # Step 1: Opening File 
    file1 = open("requirements.txt", "r") 
    
    # Step 2: Using for loop 
    for line in file1: 
        fileInput=line.strip()   
        fileContentLineKingdom = fileInput.split(' ')[0]
        fileContentLineKingdomMsg = fileInput.split(' ')[1]
        # print(fileContentLineKingdom)
        # print(fileContentLineKingdomMsg)

        checkResult=DecriptTextWithEmplem(fileContentLineKingdom,fileContentLineKingdomMsg)
        # print(checkResult)
        AddKindomToList(checkResult,fileContentLineKingdom)
   
    # Closing files 
    file1.close() 

    if(len(kindomList)>3):print(kindomList)
    else : print('NONE')
  
if __name__ == "__main__":
  main()

