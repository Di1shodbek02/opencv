import time

import cv2
from pyzbar.pyzbar import decode
from pygame import mixer

cap = cv2.VideoCapture(0)

narxlar = {
    '4780030030852':
        {
            'Salfetka': '6500'
        },
    '47800330200133': {'Chococream': '34000'},
    '4600338001302': {'FrutaNYANYA': '23000'},
    '7613031568147': {'Nestle NAN 3': '50000'},
    '9780230035362': {'Destination B1': '10000'},
    '4780040670246': {'Marwan Notebook 200x200': '12000'},
    '4780086950029': {'Copybook Book 200x200': '5000'},
}


class Scanner:

    def get_barcode(self, cam_url):
        hisoblash = 0
        umimiy_maxsulotlar = []

        cap = cv2.VideoCapture(cam_url)
        try:
            while True:
                # Kameradan tasvir olish
                ret, frame = cap.read()
                if not ret:
                    print('Kameradan tasvir olishda xato!!! Tekshirib Koring')
                    break
                frame = cv2.resize(frame, (500, 400))
                # Shtrix Kodlarni dekodlash
                decoded_objects = decode(frame)

                for obj in decoded_objects:
                    # Malumotni o'qish va consulega chiqarish
                    data = obj.data.decode('utf-8')  # Malumotni O'qish
                    print('Shtrix Kod Topildi: ', data)
                    print(type(data))
                    maxsulot = narxlar.get(data)

                    for nomi, narx in maxsulot.items():
                        hisoblash += int(narx)

                        umimiy_maxsulotlar.append(nomi)

                        print(umimiy_maxsulotlar)
                        print(f'Sizdan {hisoblash} som')

                        mixer.init()
                        sound_file = 'scan.mp3'
                        mixer.music.load(sound_file)
                        mixer.music.play()
                        time.sleep(1)

                        # Dekodlangan Malumotni atforida ramka chizish
                        (x, y, w, h) = obj.rect  # Extracting rectangle coordinates
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Shtrix kod malumotini ekranda ko'rsatish
                        text = f'{data}'
                        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


                # Natijani ko'rsatish
                cv2.imshow('Kamera', frame)

                # Agar 'q' tugmasi bosilsa, dasturni to'xtatish
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            # Kamerani va Barcha oynani yopish
            cap.release()
            cv2.destroyAllWindows()


cam = Scanner()
cam.get_barcode("http://10.10.1.205:4747/video")
