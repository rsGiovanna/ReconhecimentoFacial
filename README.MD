

# Frequência com Reconhecimento Facial

Este projeto é uma atividade extracurrícular, desenvolvido por alunos do 7° período de Sistemas de informação do Centro Universitário do Planalto Central Apparecido dos Santos (UNICEPLAC). 

O objetivo deste projeto é utilizar a tecnologia a favor professores e instituições de ensino no controle de presença de alunos.

Tem como beneficios um melhor controle dos alunos, facilitando a organização, economia de tempo, diminuição na utilização de papel, melhor desempenho e aproveitamento dos alunos visto que não poderão faltar ou estar em outro local, senão em sala.

A ideia é que, ao avançar no desenvolvimento do projeto, possamos dar um controle melhor até para os pais. Muitos pais deixam seus filhos na porta da escola e eles nem sequer entram. Caso não entrem, não estejam presentes, será emitido um alerta aos pais. Isso poderá evitar sequestros, decaimento no rendimento de alunos e os pais poderão se sentir tranquilos por saber que seus filhos estão em um local seguro.

## Instalação

Para realizar a instalação no windows, foi necessário seguir todos os passos a seguir:

1° - Instalar Python https://www.python.org/downloads/

2° - É necessário um editor de código, estamos utilizando o VSCode https://code.visualstudio.com/download

3° - No VSCode há opção de instalar extenções, instale a extensão do Python

4° - Iremos iniciar o nosso projeto:
    ```
        __No terminal__

    1 - Digite| -m venv venv 
    2 - Digite| Set-ExecutionPolicy Unrestricted -Scope Process
    3 - Digite| venv\Scripts\activate.ps1

    Aperte as teclas CTRL + SHIFT + P
    Selecione a opção| Python: Select Interpreter
    Selecione a opção| Python: 3.10.2 ('venv':venv) .\venv\Scripts\python.exe
    
    Certifique-se que os arquivos "requirements.txt" e "dlib-19.22.99-cp310-cp310-win_amd64.whl" estejam na pasta do projeto

      __No terminal__

    1 - Digite| pip install -r requirements.txt
    2 - Digite| pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
    3 - Digite| pip install face-recognition
    4 - Digite| pip install numpy
    5 - Digite| pip install opencv-python

    Para conferir se estão instalados| pip list

    Biblioteca utilizada| https://face-recognition.readthedocs.io/en/latest/readme.html
    
    ```

    
## 🚀 Sobre nós

Somos estudantes do 7° periodo de sistema de informação na UNICEPLAC.
Nosso grupo é composto por 4 integrantes, sendo eles:

Josue Neris | 20 anos de idade | Documentador do sistema| https://www.linkedin.com/in/josu%C3%A9-neri-a8743a1b6/
Mikaelle Ferreira | 21 anos de idade | Gestora do projeto| https://www.linkedin.com/in/mikaelle-ferreira-774261184/
Giovanna Rodrigues | 21 anos de idade | Desenvolvedora| https://www.linkedin.com/in/giovanna-rs/
Rodrigo Alex | 21 anos de idade | Desenvolvedor BackEnd| https://www.linkedin.com/in/rodrigo-alex-11145992/