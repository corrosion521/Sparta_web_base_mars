<h1>화성 땅 경매 </h1>

1. 기능 1 : 입력된 데이터를 db에 저장 [POST]
    1. 클라이언트 : 데이터 보낸 후( (이름,주소,평수))  메시지(alert)와 함께 새로고침
        - data out: 이름, 주소, 평수
        - data in : 메시지
    2. 서버 : 클라로부터 받아온 데이터 db저장하고, 메시지를 보내줌.
        - data in : 이름, 주소, 평수
        - data out : 메시지   
2. 기능 2: 새로고침 되자마자 리스트 업데이트[GET]
    1. 클라이언트 :  서버에서 보내온 데이터 이용해서 html요소 추가(아래 표 행들 (리스트))
        - data in: 화성 경매 리스트 데이터 
        - data out : x 
    2. 서버 : db에서 데이터 꺼내서 클라이언트에 해당 데이터(화성 경매 관련 )리스트 보내줌.
        - data in : x
        - data out : 화성 경매 리스트 데이터