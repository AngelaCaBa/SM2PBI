import os
import time
from pathlib import Path

carpeta = Path(
    r"C:\Users\ucara169\OneDrive - Yanfeng\SM 2 - Staff - Data Analyst\Ramos\Psicometria del Lider\days"
)

# Buscar PDFs
pdfs = sorted(carpeta.glob("*.pdf"))

print(f"\nPDF encontrados: {len(pdfs)}\n")

if not pdfs:
    print("No se encontraron archivos PDF.")
    input("Presiona ENTER para cerrar...")
    raise SystemExit


TAMANO_LOTE = 10


for i, pdf in enumerate(pdfs, start=1):

    try:
        print(f"[{i}/{len(pdfs)}] Imprimiendo: {pdf.name}")

        # Mandar a imprimir usando Adobe / aplicación predeterminada
        os.startfile(str(pdf), "print")

        # Pequeña pausa entre documentos
        time.sleep(3)

    except Exception as e:
        print(f"ERROR con {pdf.name}: {e}")

    # Cada 10 PDFs, detenerse
    if i % TAMANO_LOTE == 0 and i < len(pdfs):

        print("\n" + "=" * 60)
        print(f"LOTE DE {TAMANO_LOTE} PDFs ENVIADO")
        print("=" * 60)

        print("\nEspera a que la impresora termine estos documentos.")
        input("Cuando esté lista, presiona ENTER para enviar los siguientes 10...")

        print("\nContinuando...\n")


print("\n" + "=" * 60)
print("TODOS LOS PDFs FUERON ENVIADOS")
print("=" * 60)

input("\nPresiona ENTER para cerrar...")