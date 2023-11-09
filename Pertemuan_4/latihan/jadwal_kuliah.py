from prettytable import PrettyTable

def buat_jadwal_kuliah(jadwal_file, jadwal):
    with open(jadwal_file, 'w') as file:
        for hari, (mata_kuliah_list, nama_dosen_list) in jadwal.items():
            file.write(f'{hari}:\n')
            for mk, nm in zip(mata_kuliah_list, nama_dosen_list):
                file.write(f'{mk}: {nm}\n')





def baca_jadwal_kuliah(jadwal_file):
    jadwal = {}
    with open(jadwal_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                hari, jadwal_data = line.split(': ')
                jadwal_data = jadwal_data.split(', ')
                mata_kuliah = jadwal_data[0].split(', ') if jadwal_data[0] else []
                nama_dosen = jadwal_data[1].split(', ') if len(jadwal_data) > 1 and jadwal_data[1] else []
                jadwal[hari] = (mata_kuliah, nama_dosen)
            else:
                jadwal[hari] = ([], [])  # Handle empty data for a day
    return jadwal

def tampilkan_jadwal(jadwal):
    table = PrettyTable()
    table.field_names = ["Hari", "Mata Kuliah", "Nama Dosen"]

    # Create a list of days and iterate through them
    days = list(jadwal.keys())
    all_mata_kuliah = []
    all_nama_dosen = []

    for hari in days:
        mata_kuliah_list, nama_dosen_list = jadwal[hari]
        all_mata_kuliah.extend(mata_kuliah_list)
        all_nama_dosen.extend(nama_dosen_list)

    max_length = max(len(all_mata_kuliah), len(all_nama_dosen))

    for i in range(max_length):
        mata_kuliah = all_mata_kuliah[i] if i < len(all_mata_kuliah) else ""
        nama_dosen = all_nama_dosen[i] if i < len(all_nama_dosen) else ""
        current_day = days[i % len(days)]  # Use modulo to cycle through days
        table.add_row([current_day, mata_kuliah, nama_dosen])

    print(table)




def edit_jadwal(jadwal_file):
    jadwal = baca_jadwal_kuliah(jadwal_file)

    print('Jadwal Kuliah:')
    tampilkan_jadwal(jadwal)

    while True:
        print('Menu Edit:')
        print('1. Tambah Mata Kuliah')
        print('2. Tambah Nama Dosen')
        print('3. Edit Mata Kuliah')
        print('4. Hapus Mata Kuliah')
        print('5. Edit Nama Dosen')
        print('6. Hapus Nama Dosen')
        print('7. Simpan dan Keluar')

        pilihan = input('Pilih menu edit (1/2/3/4/5/6/7): ')

        if pilihan == '1':
            hari = input('Hari: ')
            mata_kuliah = input('Mata Kuliah: ')
            if hari in jadwal:
                if mata_kuliah not in jadwal[hari][0]:
                    jadwal[hari][0].append(mata_kuliah)
                else:
                    print('Mata Kuliah sudah ada dalam jadwal.')
            else:
                jadwal[hari] = ([mata_kuliah], jadwal.get(hari, ([], [])[1]))  # Create a new entry for the day if it doesn't exist
        elif pilihan == '2':
            hari = input('Hari: ')
            nama_dosen = input('Nama Dosen: ')
            if hari in jadwal:
                if nama_dosen not in jadwal[hari][1]:
                    jadwal[hari][1].append(nama_dosen)
                else:
                    print('Nama Dosen sudah ada dalam jadwal.')
            else:
                jadwal[hari] = (jadwal.get(hari, ([], [])[0], [nama_dosen]))  # Create a new entry for the day if it doesn't exist
        elif pilihan == '3':
            hari = input('Hari: ')
            if hari in jadwal:
                print(f'Mata Kuliah pada {hari}: {", ".join(jadwal[hari][0])}')
                mata_kuliah_lama = input('Mata Kuliah Lama: ')
                mata_kuliah_baru = input('Mata Kuliah Baru: ')
                if mata_kuliah_lama in jadwal[hari][0]:
                    index = jadwal[hari][0].index(mata_kuliah_lama)
                    jadwal[hari][0][index] = mata_kuliah_baru
                else:
                    print('Mata Kuliah tidak ditemukan.')
            else:
                print(f'Hari {hari} tidak ditemukan dalam jadwal.')
        elif pilihan == '4':
            hari = input('Hari: ')
            if hari in jadwal:
                print(f'Mata Kuliah pada {hari}: {", ".join(jadwal[hari][0])}')
                mata_kuliah_hapus = input('Mata Kuliah yang ingin dihapus: ')
                if mata_kuliah_hapus in jadwal[hari][0]:
                    jadwal[hari][0].remove(mata_kuliah_hapus)
                    if not jadwal[hari][0]:
                        del jadwal[hari]
                else:
                    print('Mata Kuliah tidak ditemukan.')
            else:
                print(f'Hari {hari} tidak ditemukan dalam jadwal.')
        elif pilihan == '5':
            hari = input('Hari: ')
            if hari in jadwal:
                print(f'Nama Dosen pada {hari}: {", ".join(jadwal[hari][1])}')
                nama_dosen_lama = input('Nama Dosen Lama: ')
                nama_dosen_baru = input('Nama Dosen Baru: ')
                if nama_dosen_lama in jadwal[hari][1]:
                    index = jadwal[hari][1].index(nama_dosen_lama)
                    jadwal[hari][1][index] = nama_dosen_baru
                else:
                    print('Nama Dosen tidak ditemukan.')
            else:
                print(f'Hari {hari} tidak ditemukan dalam jadwal.')
        elif pilihan == '6':
            hari = input('Hari: ')
            if hari in jadwal:
                print(f'Nama Dosen pada {hari}: {", ".join(jadwal[hari][1])}')
                nama_dosen_hapus = input('Nama Dosen yang ingin dihapus: ')
                if nama_dosen_hapus in jadwal[hari][1]:
                    jadwal[hari][1].remove(nama_dosen_hapus)
                    if not jadwal[hari][1]:
                        del jadwal[hari]
                else:
                    print('Nama Dosen tidak ditemukan.')
            else:
                print(f'Hari {hari} tidak ditemukan dalam jadwal.')
        elif pilihan == '7':
            with open(jadwal_file, 'w') as file:
                for hari, (mata_kuliah_list, nama_dosen_list) in jadwal.items():
                    mata_kuliah_str = ', '.join(mata_kuliah_list)
                    nama_dosen_str = ', '.join(nama_dosen_list)
                    file.write(f'{hari}: {mata_kuliah_str}, {nama_dosen_str}\n')
            break
        else:
            print('Pilihan tidak valid. Silakan pilih menu yang benar.')

def main():
    jadwal_file = 'jadwal_kuliah.txt'

    while True:
        print('Menu:')
        print('1. Buat Jadwal Kuliah')
        print('2. Tampilkan Jadwal Kuliah')
        print('3. Edit Jadwal Kuliah')
        print('4. Keluar')

        pilihan = input('Pilih menu (1/2/3/4): ')

        if pilihan == '1':
            jadwal = {}  # Initialize an empty schedule dictionary
            buat_jadwal_kuliah(jadwal_file, jadwal)
            print('Jadwal kuliah telah dibuat dan disimpan di', jadwal_file)
        elif pilihan == '2':
            jadwal = baca_jadwal_kuliah(jadwal_file)
            tampilkan_jadwal(jadwal)  # Pass 'jadwal' to the function
        elif pilihan == '3':
            edit_jadwal(jadwal_file)
            print('Jadwal kuliah telah diperbarui dan disimpan di', jadwal_file)
        elif pilihan == '4':
            break
        else:
            print('Pilihan tidak valid. Silakan pilih menu yang benar.')

if __name__ == '__main__':
    main()