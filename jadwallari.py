
def pembuatan_jadwal_lari():
    # Start
        # Print Session
            print('=' *35)
            print('Halo Pengguna, aku adalah program yang akan membantu kamu \n' \
            'membuat jadwal latihan. ><')
        # Data setion
import re
def klasifikasi(teks):
        # Cari angka
                angka = re.findall(r'\d+', teks)
                angka = int(angka[0]) if angka else 0
        # Deteksi satuan
                if 'tahun' in teks.lower():
                        total_bulan = angka * 12
                        satuan = 'tahun'
                elif 'bulan' in teks.lower():
                        total_bulan = angka
                        satuan = 'bulan'
                else:
                        total_bulan = angka
                        satuan = 'tidak diketahui'
        # Tentukan kategori
                        if total_bulan < 12:
                                kategori = 'Pemula'
                        elif 12 <= total_bulan <= 36:
                                kategori = 'Menengah'
                        else:
                                kategori = 'Ahli'
        # Bentuk Dictionary asli
                        hasil = {
                                'input_asli':teks,
                                'angka':angka,
                                'satuan':satuan,
                                'total_bulan':total_bulan
                        }

        # Input session
def pertanyaan():
            pertanyaan_1 = input('Sudah berapa lama kamu latihan? : [1-3, lainnya]').lower()
            pertanyaan_2 = input('Berapa kali kamu latihan dalam seminggu? [2x, 4x, lainnya]').lower()
            pertanyaan_3 = input('kesibukan apa selain berlari? [Pekerja, Mahasiswa, Pelajar, lainnya]').lower()
            pertanyaan_4 = input('Apa yang ingin kamu capai? [Marathon, Halfmarathon, 10k, 5k, Memperbaiki jadwal latihan]').lower()
        # pengkondisian
while True:
        jawaban = input('Apakah kamu ingin melanjutkan (iya/tidak)\n'
        'Berikan jawaban kamu = ').lower()
        if jawaban == 'iya':
            print('Baguus, aku akam mengajukan beberapa pertanyaan, kamu jawab sesuai degan kepribadian kamu yaa')
            pertanyaan()
        elif jawaban == 'tidak':
            print('Terimakasih sudah berkunjung')
        else:
            print('Aku Rasa.. Kamu memasukan input yang salah...')
            break
        
                
pembuatan_jadwal_lari()
