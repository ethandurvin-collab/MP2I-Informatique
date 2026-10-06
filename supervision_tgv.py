"""Supervision TGV autonome - version simple (2 modules : Sécurité et Réseau)."""
import random
import tkinter as tk


def analyse_IA(vitesse, porte_fermee, lidar_obstacle, mvb, gsmr, frmcs):
    if not porte_fermee or lidar_obstacle or not mvb or (not gsmr and not frmcs):
        return "🚨 DANGER", "red"
    if vitesse > 300:
        return "⚠️ ALERTE", "orange"
    return "✅ OK", "green"


def maj():
    #variable aleatoire 
    vitesse = random.randint(0, 320)
    porte_fermee = random.random() > 0.1
    lidar_obstacle = random.random() < 0.1
    mvb = random.random() > 0.05
    ethernet = random.random() > 0.05
    gsmr = random.random() > 0.2
    frmcs = random.random() > 0.1
    
    #affichage dans les labbels
    l_vitesse.config(text=f"Vitesse : {vitesse} km/h")
    l_porte.config(text="Portes : " + ("✅ fermées" if porte_fermee else "🚨 ouverte"))
    l_lidar.config(text="LIDAR : " + ("🚨 obstacle" if lidar_obstacle else "✅ voie libre"))
    l_mvb.config(text="MVB (interne) : " + ("✅" if mvb else "🚨"))
    l_ethernet.config(text="Ethernet train (interne) : " + ("✅" if ethernet else "🚨"))
    l_gsmr.config(text="GSM-R (sol-train) : " + ("✅" if gsmr else "🚨"))
    l_frmcs.config(text="FRMCS (sol-train) : " + ("✅" if frmcs else "🚨"))

    texte, couleur = analyse_IA(vitesse, porte_fermee, lidar_obstacle, mvb, gsmr, frmcs)
    l_etat.config(text=texte, bg=couleur)
    fenetre.after(2000, maj)


fenetre = tk.Tk()
fenetre.title("Supervision TGV")

l_vitesse = tk.Label(fenetre, font=("Arial", 20))
l_vitesse.pack(pady=5)

# Module Sécurité
cadre_sec = tk.LabelFrame(fenetre, text="Sécurité")
cadre_sec.pack(fill="x", padx=10, pady=5)
l_porte = tk.Label(cadre_sec)
l_porte.pack(anchor="w")
l_lidar = tk.Label(cadre_sec)
l_lidar.pack(anchor="w")

# Module Réseau
cadre_res = tk.LabelFrame(fenetre, text="Réseau")
cadre_res.pack(fill="x", padx=10, pady=5)
l_mvb = tk.Label(cadre_res)
l_mvb.pack(anchor="w")
l_ethernet = tk.Label(cadre_res)
l_ethernet.pack(anchor="w")
l_gsmr = tk.Label(cadre_res)
l_gsmr.pack(anchor="w")
l_frmcs = tk.Label(cadre_res)
l_frmcs.pack(anchor="w")

# État global
l_etat = tk.Label(fenetre, font=("Arial", 22, "bold"), fg="white", width=15, pady=10)
l_etat.pack(pady=10)

maj()
fenetre.mainloop()