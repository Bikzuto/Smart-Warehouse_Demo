import streamlit as st

from PIL import Image
from collections import Counter

st.set_page_config(page_title="Smart Warehouse Demo", layout="wide")


st.title("Route Optimization Algorithm (Demo Version)")

inventory = {
    "A": {"qty": 100, "weight": 40, "zone": "A", "shelf": 2, "loc": (1, 4)},
    "B": {"qty": 100, "weight": 8, "zone": "C", "shelf": 2, "loc": (2, 3)},
    "C": {"qty": 100, "weight": 25, "zone": "C", "shelf": 1, "loc": (2, 1)},
    "D": {"qty": 100, "weight": 40, "zone": "C", "shelf": 1, "loc": (5, 2)},
    "E": {"qty": 100, "weight": 20, "zone": "B", "shelf": 4, "loc": (4, 9)},
    "F": {"qty": 100, "weight": 20, "zone": "B", "shelf": 3, "loc": (4, 4)},
    "G": {"qty": 100, "weight": 10, "zone": "C", "shelf": 6, "loc": (3, 5)},
    "H": {"qty": 100, "weight": 35, "zone": "A", "shelf": 5, "loc": (4, 6)}
}


st.subheader("Our Warehouse Layout Idea")


col1, col2, col3 = st.columns([1, 2, 1]) # Adjust column ratios as needed

with col1:
    st.write(' ') # Empty space

with col2:
    img = Image.open("finalwarehouse.jpg")
    st.image(img, width = 800)

with col3:
    st.write(' ') 








st.header("Input Order")

col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("A", 0)
    d = st.number_input("D", 0)
    g = st.number_input("G", 0)

with col2:
    b = st.number_input("B", 0)
    e = st.number_input("E", 0)
    h = st.number_input("H", 0)

with col3:
    c = st.number_input("C", 0)
    f = st.number_input("F", 0)
    

order_dict = {
    "A": a,
    "B": b,
    "C": c,
    "D": d,
    "E": e,
    "F": f,
    "G": g,
    "H": h
}


order_items = []
for item, qty in order_dict.items():
    if qty > 0:
        order_items.append(item)


st.header("Optimized Picking Route")

if order_items:
    sorted_items = sorted(order_items, key=lambda x: inventory[x]["loc"])

    for i, item in enumerate(sorted_items):
        zone = inventory[item]["zone"]
        shelf = inventory[item]["shelf"]

        if zone == "A":
            st.info(f"Step {i+1}: Pick {item} → Zone {zone}, Shelf {shelf}")
        elif zone == "B":
            st.success(f"Step {i+1}: Pick {item} → Zone {zone}, Shelf {shelf}")
        else:
            st.error(f"Step {i+1}: Pick {item} → Zone {zone}, Shelf {shelf}")

else:
    st.write("*** Please input order ***")


st.header("Summary")


zones = set([inventory[i]['zone'] for i in order_items])
zones_text = ", ".join(zones)

st.write(f"Zones involved: {zones_text}")



st.write("Item quantity:")
for item, qty in order_dict.items():
    if qty > 0:
        weight = inventory[item]["weight"]
        st.write(f"{item} = {qty} Unit / Total {item} weight: {qty * weight} kg")

allweight = (a*40) + (b*8) + (c*25) + (d*40) + (e*20) + (f*20) + (g*10)+ (h*35)
st.write(f"Overall weight: ", allweight, "kg")
st.write("> A = 40 kg/Units , B = 8 kg/Units , C = 25 kg/Units , D = 40 kg/Units   ,   E = 20 kg/Units , F = 20 kg/Units , G = 10 kg/Units , H = 35 kg/Units")