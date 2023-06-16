import tkinter as tk
import tkinter.messagebox as messagebox

def logo():
    logo_text = " __  __ ______ _____ _____           _____ ______ _______ \n" \
                "|  \/  |  ____|  __ \_   _|   /\    / ____|  ____|__   __|\n" \
                "| \  / | |__  | |  | || |    /  \  | (___ | |__     | |   \n" \
                "| |\/| |  __| | |  | || |   / /\ \  \___ \|  __|    | |   \n" \
                "| |  | | |____| |__| || |_ / ____ \ ____) | |____   | |   \n" \
                "|_|  |_|______|_____/_____/_/    \_\_____/|______|  |_|   "
    logo_label = tk.Label(window, text=logo_text, font=("Courier New", 14), justify="left")
    logo_label.pack()

def handle_choice(choice):
    if choice == "1":
        template1()
    elif choice == "2":
        template2()
    elif choice == "3":
        template3()
    elif choice == "4":
        template4()
    elif choice == "5":
        template5()
    elif choice == "6":
        template6()
    elif choice == "7":
        template7()
    elif choice == "8":
        template8()
    elif choice == "9":
        template9()
    elif choice == "10":
        template10()

def template1():
    nome_label = tk.Label(window, text="Inserisci il nome dell'utente (ex. Mario Rossi):")
    nome_label.pack()
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    email_label = tk.Label(window, text="Inserisci l'email dell'utente:")
    email_label.pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    def submit():
        nome = nome_entry.get()
        email = email_entry.get()

        richiesta1 = f"@GG: Si richiede di abilitare all'utilizzo di OnAir Produzione, l'utente: {nome}"
        richiesta1a = f"@Assistenza: Si richiede di installare l'applicativo OnAir Produzione all'utente: {email}"
        richiesta1b = f"@Giovanna.candura@mediaset.it: Si richiede di abilitare all'utilizzo di OnAir Produzione, l'utente: {nome}, {email}"
        output_text = f"{richiesta1}\n{richiesta1a}\n{richiesta1b}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template2():
    nome_label = tk.Label(window, text="Inserisci il nome dell'utente (ex. Mario Rossi):")
    nome_label.pack()
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    email_label = tk.Label(window, text="Inserisci l'email dell'utente:")
    email_label.pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    gruppo_label = tk.Label(window, text="Inserisci il gruppo/i dell'utente:")
    gruppo_label.pack()
    gruppo_entry = tk.Entry(window)
    gruppo_entry.pack()

    share1_label = tk.Label(window, text="Inserisci il nome della prima share:")
    share1_label.pack()
    share1_entry = tk.Entry(window)
    share1_entry.pack()

    share2_label = tk.Label(window, text="Inserisci il nome della seconda share (opzionale):")
    share2_label.pack()
    share2_entry = tk.Entry(window)
    share2_entry.pack()

    share3_label = tk.Label(window, text="Inserisci il nome della terza share (opzionale):")
    share3_label.pack()
    share3_entry = tk.Entry(window)
    share3_entry.pack()

    share4_label = tk.Label(window, text="Inserisci il nome della quarta share (opzionale):")
    share4_label.pack()
    share4_entry = tk.Entry(window)
    share4_entry.pack()

    def submit():
        nome = nome_entry.get()
        email = email_entry.get()
        gruppo = gruppo_entry.get()
        share1 = share1_entry.get()
        share2 = share2_entry.get()
        share3 = share3_entry.get()
        share4 = share4_entry.get()

        richiesta2 = f"@AM: Si richiede assegnazione PC desktop + monitor + mouse + tastiera per l'utente: {nome}, {email}"
        richiesta2a = f"@GP: Si richiede l'assegnazione di una licenza E3 per l'utente: {email}"
        richiesta2b = f"@GG: Si richiede di abilitare al gruppo/i {gruppo} l'utente: {email}"
        richiesta2c = f"@GG: Si richiede di abilitare l'utente {nome} in lettura/scrittura alle seguenti cartelle di rete: {share1} {share2} {share3} {share4}"
        output_text = f"{richiesta2}\n{richiesta2a}\n{richiesta2b}\n{richiesta2c}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template3():
    nome_label = tk.Label(window, text="Inserisci il nome dell'utente:")
    nome_label.pack()
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    via_label = tk.Label(window, text="Inserisci la via dell'utente:")
    via_label.pack()
    via_entry = tk.Entry(window)
    via_entry.pack()

    cap_label = tk.Label(window, text="Inserisci il CAP dell'utente:")
    cap_label.pack()
    cap_entry = tk.Entry(window)
    cap_entry.pack()

    citta_label = tk.Label(window, text="Inserisci la città dell'utente:")
    citta_label.pack()
    citta_entry = tk.Entry(window)
    citta_entry.pack()

    provincia_label = tk.Label(window, text="Inserisci la provincia dell'utente:")
    provincia_label.pack()
    provincia_entry = tk.Entry(window)
    provincia_entry.pack()

    def submit():
        nome = nome_entry.get()
        via = via_entry.get()
        cap = cap_entry.get()
        citta = citta_entry.get()
        provincia = provincia_entry.get()

        richiesta3 = f"{nome}\nVia {via}\nCAP {cap} Città {citta} Provincia {provincia}"
        output_text = richiesta3
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template4():
    nome_label = tk.Label(window, text="Inserisci il nome dell'utente:")
    nome_label.pack()
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    def submit():
        nome = nome_entry.get()

        richiesta4 = f"@GG: Inserire l'utenza {nome} del gruppo IPAM_AZURE"
        richiesta4a = "Promemoria per @GG: Inviare mail @Donato Tagliabue con CC Fabio Rossi per creazione account."
        output_text = f"{richiesta4}\n{richiesta4a}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template5():
    nome_label = tk.Label(window, text="Inserisci il nome dell'utente:")
    nome_label.pack()
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    codice_ct_label = tk.Label(window, text="Inserisci il codice CT dell'utente:")
    codice_ct_label.pack()
    codice_ct_entry = tk.Entry(window)
    codice_ct_entry.pack()

    telefono_label = tk.Label(window, text="Inserisci il telefono dell'utente:")
    telefono_label.pack()
    telefono_entry = tk.Entry(window)
    telefono_entry.pack()

    def submit():
        nome = nome_entry.get()
        codice_ct = codice_ct_entry.get()
        telefono = telefono_entry.get()

        richiesta5 = f"@GG: Si richiede di inserire l'utente {codice_ct} nei gruppi VPN_Mobile e VPN_Fornitori_Mediaset e qualora esista nel gruppo VPN dedicato."
        richiesta5a = f"@Assistenza: Generare certificato VPN per l'utente {nome} (TEL: {telefono})."
        richiesta5b = f"@Assistenza: Generato certificato VPN."
        richiesta5c = f"Creata utenza di dominio, abilitata utenza alla VPN.\nInviato certificato ed inviate credenziali direttamente al referente dell'utente.\nLa password del certificato VPN è stata inviata via SMS direttamente all'utente."
        output_text = f"{richiesta5}\n{richiesta5a}\n{richiesta5b}\n{richiesta5c}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template6():
    email_label = tk.Label(window, text="Inserisci l'email dell'utente:")
    email_label.pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    client_label = tk.Label(window, text="Inserisci il/i client ibridi:")
    client_label.pack()
    client_entry = tk.Entry(window)
    client_entry.pack()
    
    def submit():
        email = email_entry.get()
        client = client_entry.get()

        richiesta6 = f"@GG: Si richiede di inserire le seguenti utenze nel gruppo VPN_RDP e nel gruppo VPN_RDP_SERVICE: {email}."
        richiesta6a = f"E i seguenti client al gruppo CLIENT_RDP_ENABLE: {client}"
        output_text = f"{richiesta6}\n{richiesta6a}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template7():
    email_label = tk.Label(window, text="Inserisci l'email dell'utente:")
    email_label.pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    client_label = tk.Label(window, text="Inserisci il/i client Azure:")
    client_label.pack()
    client_entry = tk.Entry(window)
    client_entry.pack()

    def submit():
        email = email_entry.get()
        client = client_entry.get()

        richiesta7 = f"@GG: Si richiede di inserire le seguenti utenze nel gruppo VPN_RDP e nel gruppo VPN_RDP_SERVICE: {email}."
        richiesta7a = f"Si richiede di inserire i seguenti client nel gruppo AZURE MDMW_DEV_RDP_Enable_Static: {client}"
        output_text = f"{richiesta7}\n{richiesta7a}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()
def template8():
    nome_label = tk.Label(window, text="Inserisci il nome dell'utente:")
    nome_label.pack()
    nome_entry = tk.Entry(window)
    nome_entry.pack()

    cespite_label = tk.Label(window, text="Inserisci il cespite:")
    cespite_label.pack()
    cespite_entry = tk.Entry(window)
    cespite_entry.pack()

    def submit():
        nome = nome_entry.get()
        cespite = cespite_entry.get()

        richiesta8 = f"@CC: Si richiede di sbloccare l`accesso al portale PIM per il PC assegnato all`utente: {nome} con cespite {cespite}."
        richiesta8a = f"Abilitare Utente nel Gruppo MDMW_USR_WNP_Users per abilitazione TLS 1.0"
        output_text = f"{richiesta8}\n{richiesta8a}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template9():
    modello_label = tk.Label(window, text="Inserisci il modello:")
    modello_label.pack()
    modello_entry = tk.Entry(window)
    modello_entry.pack()

    seriale_label = tk.Label(window, text="Inserisci il seriale:")
    seriale_label.pack()
    seriale_entry = tk.Entry(window)
    seriale_entry.pack()

    sku_label = tk.Label(window, text="Inserisci il numero SKU:")
    sku_label.pack()
    sku_entry = tk.Entry(window)
    sku_entry.pack()

    cespite_label = tk.Label(window, text="Inserisci il cespite:")
    cespite_label.pack()
    cespite_entry = tk.Entry(window)
    cespite_entry.pack()

    def submit():
        modello = modello_entry.get()
        seriale = seriale_entry.get()
        sku = sku_entry.get()
        cespite = cespite_entry.get()

        richiesta9 = f"@GP: a seguito di smarrimento del dispositivo aziendale si richiede ultimo accesso a Office 365 di:\nModello: {modello}\nSeriale: {seriale}\nNumero SKU: {sku}\nCespite: {cespite}."
        output_text = richiesta9
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def template10():
    email_label = tk.Label(window, text="Inserisci email dell'utente:")
    email_label.pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    inizio_label = tk.Label(window, text="Inserisci data di inizio roaming(gg/mm/aaaa):")
    inizio_label.pack()
    inizio_entry = tk.Entry(window)
    inizio_entry.pack()

    fine_label = tk.Label(window, text="Inserisci data di fine roaming (gg/mm/aaaa):")
    fine_label.pack()
    fine_entry = tk.Entry(window)
    fine_entry.pack()

    telefono_label = tk.Label(window, text="Inserisci il telefono dell'utente:")
    telefono_label.pack()
    telefono_entry = tk.Entry(window)
    telefono_entry.pack()

    def submit():
        email= email_entry.get()
        inizio = inizio_entry.get()
        fine = fine_entry.get()
        telefono = telefono_entry.get()

        richiesta10 = f"@GG: Si richiede di abilitare {email} al gruppo MFA_AzureAD_WorldWide_Users."
        richiesta10a =f"@Fonia: Si richiede di abilitare {email} dal {inizio} al {fine} al roaming internazionale (Telefono: {telefono})."
        output_text = f"{richiesta10}\n{richiesta10a}"
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_label = tk.Label(output_window, text=output_text, font=("Courier New", 12), justify="left")
        output_label.pack()
        copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(output_text))
        copy_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

def copy_to_clipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("Copy", "Template copiato negli appunti!")

window = tk.Tk()
window.title("Script di Generazione Templates - By Tommaso Bona")

logo()

instructions_label = tk.Label(window, text="Scegli un template:\n1) Template OnAir Production\n2) Template Nuovo Utente\n3) Template Richiesta Monitor\n4) Template Richiesta IPAM Azure\n5) Template Richiesta VPN Fornitori\n6) Template Abilitazione RDP Ibrido\n7) Template Abilitazione RDP Azure\n8) Template Abilitazione PIM\n9)Template Furto/Smarrimento Dispositivo\n10) Template MFA_AzureAD_WorldWide_Users")
instructions_label.pack()

choice_entry = tk.Entry(window)
choice_entry.pack()

submit_button = tk.Button(window, text="Submit", command=lambda: handle_choice(choice_entry.get()))
submit_button.pack()

window.mainloop()
