import face_recognition  # importar biblioteca de reconhcimento facial
import cv2  # importar biblioteca opencv
import numpy as np  # importar biblioteca numpy
import csv  # importar biblioteca para gravar dados em arquivo csv

# função para capturar imagem
video_capture = cv2.VideoCapture(0)

# carregue uma imagem
rodrigo_image = face_recognition.load_image_file("img/rodrigo.jpg")
rodrigo_face_encoding = face_recognition.face_encodings(rodrigo_image)[0]

gilmar_image = face_recognition.load_image_file("img/gilmar.jpg")
gilmar_face_encoding = face_recognition.face_encodings(gilmar_image)[0]

mikaelle_image = face_recognition.load_image_file("img/mikaelle.jpg")
mikaelle_face_encoding = face_recognition.face_encodings(mikaelle_image)[0]

josue_image = face_recognition.load_image_file("img/josue.jpg")
josue_face_encoding = face_recognition.face_encodings(josue_image)[0]

giovanna_image = face_recognition.load_image_file("img/giovanna.jpg")
giovanna_face_encoding = face_recognition.face_encodings(giovanna_image)[0]


# Cria arrays de codificações de face conhecidas e seus nomes
known_face_encodings = [
    rodrigo_face_encoding,
    gilmar_face_encoding,
    mikaelle_face_encoding,
    josue_face_encoding,
    giovanna_face_encoding,
]

# cria array de nomes
known_face_names = [
    "Rodrigo ",
    "Gilmar ",
    "Mikaelle ",
    "Josue ",
    "Giovanna ",
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# loop para capturar imagens
while True:
# Pegue um único quadro de vídeo
    ret, frame = video_capture.read()

# Redimensione o quadro do vídeo para 1/4 do tamanho para processamento de reconhecimento de rosto mais rápido
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

# Converte a imagem da cor BGR (que o OpenCV usa) para a cor RGB (que usa o face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]

# Processe apenas todos os outros quadros de vídeo para economizar tempo
    if process_this_frame:
# Encontre todos os rostos e codificações de rosto no quadro atual do vídeo
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
        rgb_small_frame, face_locations)

# Crie um array de nomes de pessoas para cada localização de rosto
    face_names = []
    for face_encoding in face_encodings:
# Veja se o rosto é compatível com o(s) rosto(s) conhecido(s)
        matches = face_recognition.compare_faces(
    known_face_encodings, face_encoding)
        name = "Não reconhecido"

# Se uma correspondência foi encontrada em known_face_encodings, apenas use a primeira.
# se True nas correspondências:
###     first_match_index = matches.index(True)
###     name = known_face_names[first_match_index]

# Ou, em vez disso, use a face conhecida com a menor distância até a nova face
    face_distances = face_recognition.face_distance(
        known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
# Adicione o nome da pessoa ao array de nomes
    face_names.append(name)
# Atualize o quadro de vídeo
    process_this_frame = not process_this_frame

# Mostra os resultados
    for (top, right, bottom, left), name in zip(face_locations, face_names):
# Redimensionar os locais de rosto, pois o quadro em que detectamos foi dimensionado para 1/4 do tamanho
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

# Desenhe uma caixa ao redor do rosto
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

# Desenhe uma etiqueta com um nome abaixo do rosto
    cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6),
    font, 1.0, (255, 255, 255), 1)

# Mostre o quadro de vídeo
    cv2.imshow('Video', frame)

# Se a tecla 'esc' for pressionada, saia do loop
    if cv2.waitKey(5) == 27:  # 27 é igual a "esc"
        break  # Quando o loop acaba, feche o vídeo

with open('data/freq.csv', 'r', encoding='UTF8') as csvfile:
    leitor = csv.reader(csvfile)
    linhas = 0 # inicia em 0
    for coluna in leitor:
        if linhas == 0:
            print(f'Coluna: {" ".join(coluna)}')
            linhas += 1
        else:
            if coluna[0] == 'Rodrigo':
                rodrigo_freq = int(coluna[1])
            elif coluna[0] == 'Gilmar':
                gilmar_freq = int(coluna[1])
            elif coluna[0] == 'Mikaelle':
                mikaelle_freq = int(coluna[1])
            elif coluna[0] == 'Josue':
                josue_freq = int(coluna[1])
            elif coluna[0] == 'Giovanna':
                giovanna_freq = int(coluna[1])
            linhas += 1
leitor.writerows(giovanna_face_encoding)

with open('data/freq.csv', 'w', encoding='UTF8') as csvfile:
    writer = csv.writer(csvfile)
writer.writerows(giovanna_face_encoding)



# Feche o vídeo
video_capture.release()
# Feche a janela do vídeo
cv2.destroyAllWindows()
