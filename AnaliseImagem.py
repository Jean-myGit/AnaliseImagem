#pip install boto3

import boto3
import json
from PIL import Image

from config import id_aws, passw_aws

def recognize_celebrities(photo):

    

    # Acessando o serviço Amazon AWS com as informações do login
    client = boto3.client(
        service_name = 'rekognition',
        region_name = 'us-east-1',
        aws_access_key_id = id_aws,
        aws_secret_access_key = passw_aws

    )

    # Enviando Imagem para o serviço AWS REKOGNITION para obter informações
    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image = {'Bytes': image.read()})

    # Obtendo Resultados
    for celebrity in response['CelebrityFaces']:
        print('\n Nome: ' + celebrity['Name'])
        print(' id: ' + celebrity['Id'])
        print(' Posição:')
        print(' Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print(' Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print(' Info')
        for url in celebrity['Urls']:
            print('   ' + url)
        print()
    return len(response['CelebrityFaces'])


def main():
    photo = input("Digite o Local onde está a Imgem: ")
    

    celeb_count = recognize_celebrities(photo)
    print("\n Pessoas detectadas: " + str(celeb_count))
    
    im = Image.open(photo)
  
    im.show()
    
    input()


if __name__ == "__main__":
    main()
