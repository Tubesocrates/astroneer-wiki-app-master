#INSERT ITEM LIST IN A GRID FORMAT
#ITEM ICON | ITEM NAME | SMELTED | ATHMOSPHERIC CONDENSOR | CHEM LAB USED IN

__author__ = 'chrismelnyk'
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import font

root = tk.Tk()
root.geometry('700x600')
root.title('Build List')

icon_img = 'images/icon_astro.jpg'
icon = ImageTk.PhotoImage(Image.open(icon_img))
root.tk.call('wm','iconphoto', root._w, icon)

#               OBJECTS
img_atmos = "images/build/atmos_conden.png"
img_battery = "images/build/battery.png"
img_beacon = "images/build/beacon.png"
img_cannister = "images/build/cannister.png"
img_chem = "images/build/chem_lab.png"
img_crane = "images/build/crane.png"
img_drill = "images/build/drill_head.png"
img_dynamite = "images/build/dynamite.png"
img_extenders = "images/build/extenders.png"
img_fireworks = "images/build/fireworks.png"
img_thruster = "images/build/fuel_thruster.png"
img_generator = "images/build/generator.png"
img_landing = "images/build/landing_pad.png"
img_lg_print = "images/build/large_printer.png"
img_md_print = "images/build/medium_printer.png"
img_sml_print = "images/build/small_printer.png"
img_mod = "images/build/mod.png"
img_oxy_tank = "images/build/oxygen.png"
img_oxygenator = "images/build/oxygenator.png"
img_packager = "images/build/packager.png"
img_platform = "images/build/platform.png"
img_power = "images/build/power_cells.png"
img_research = "images/build/research.png"
img_seat = "images/build/rover_seat.png"
img_shelter = "images/build/shelter.png"
img_shredder = "images/build/shredder.png"
img_shuttle = "images/build/shuttle.png"
img_smelt = "images/build/smelt.png"
img_soil = "images/build/soil.png"
img_solar = "images/build/solar_panel.png"
img_tether = "images/build/tether.png"
img_trade = "images/build/trade.png"
img_vehicle = "images/build/vehicle.png"
img_winch = "images/build/winch.png"
img_wind = "images/build/wind_turbine.png"
img_worklight = "images/build/worklight.png"

#               RAW MATERIALS
img_comound = "images/resources/compound.png"
img_resin = "images/resources/resin.png"
img_organic = "images/resources/organic.png"
img_clay = "images/resources/clay.png"
img_graphite = "images/resources/graphite.png"
img_quartz = "images/resources/quartz.png"
img_laterite = "images/resources/laterite.png"
img_sphalerite = "images/resources/sphalerite.png"
img_malachite = "images/resources/malachite.png"
img_wolframite = "images/resources/wolframite.png"
img_titanite = "images/resources/titanite.png"
img_hermatite = "images/resources/hematite.png"
img_ammonium = "images/resources/ammonium.png"
img_astronium = "images/resources/astronium.png"
img_lithium = "images/resources/lithium.png"
#             REFINED MATERIALS
img_aluminium = 'images/refined/aluminum.png'
img_carbon = 'images/refined/carbon.png'
img_ceramic= 'images/refined/ceramic.png'
img_copper= 'images/refined/copper.png'
img_glass= 'images/refined/glass.png'
img_iron= 'images/refined/iron.png'
img_titanium= 'images/refined/titanium.png'
img_tungsten= 'images/refined/tungsten.png'
img_zinc= 'images/refined/zinc.png'
#            COMPOSITE RESOURCES
img_aluminium_alloy = 'images/composite/aluminum_alloy.png'
img_diamond = 'images/composite/diamond.png'
img_explosive_powder = 'images/composite/explosive_powder.png'
img_hydrazine = 'images/composite/hydrazine.png'
img_nanocarbon_alloy = 'images/composite/nanocarbon_alloy.png'
img_plastic = 'images/composite/plastic.png'
img_rubber = 'images/composite/rubber.png'
img_silicone = 'images/composite/silicone.png'
img_steel = 'images/composite/steel.png'
img_titanium_alloy = 'images/composite/titanium_alloy.png'
img_tungsten_carbide = 'images/composite/tungsten_carbide.png'
img_graphene = 'images/composite/graphene.png'
#                   GASES
img_hydrogen = "images/gases/hydrogen.png"
img_nitrogen = "images/gases/nitrogen.png"
img_helium = "images/gases/helium.png"
img_methane = "images/gases/methane.png"
img_sulfur = "images/gases/sulfur.png"
img_argon = "images/gases/argon.png"

#              LOAD ALL IMAGES
#Objects
atmos_icon = ImageTk.PhotoImage(Image.open(img_atmos))
battery_icon = ImageTk.PhotoImage(Image.open(img_battery))
beacon_icon = ImageTk.PhotoImage(Image.open(img_beacon))
cannister_icon = ImageTk.PhotoImage(Image.open(img_cannister))
chem_icon = ImageTk.PhotoImage(Image.open(img_chem))
crane_icon = ImageTk.PhotoImage(Image.open(img_crane))
drill_icon = ImageTk.PhotoImage(Image.open(img_drill))
dynamite_icon = ImageTk.PhotoImage(Image.open(img_dynamite))
extenders_icon = ImageTk.PhotoImage(Image.open(img_extenders))
fireworks_icon = ImageTk.PhotoImage(Image.open(img_fireworks))
thruster_icon = ImageTk.PhotoImage(Image.open(img_thruster))
generator_icon = ImageTk.PhotoImage(Image.open(img_generator))
landing_icon = ImageTk.PhotoImage(Image.open(img_landing))
lg_print_icon = ImageTk.PhotoImage(Image.open(img_lg_print))
md_print_icon = ImageTk.PhotoImage(Image.open(img_md_print))
sml_print_icon = ImageTk.PhotoImage(Image.open(img_sml_print))
mod_icon = ImageTk.PhotoImage(Image.open(img_mod))
oxy_tank_icon = ImageTk.PhotoImage(Image.open(img_oxy_tank))
oxygenator_icon = ImageTk.PhotoImage(Image.open(img_oxygenator))
packager_icon = ImageTk.PhotoImage(Image.open(img_packager))
platform_icon = ImageTk.PhotoImage(Image.open(img_platform))
power_icon = ImageTk.PhotoImage(Image.open(img_power))
research_icon = ImageTk.PhotoImage(Image.open(img_research))
seat_icon = ImageTk.PhotoImage(Image.open(img_seat))
shelter_icon = ImageTk.PhotoImage(Image.open(img_shelter))
shredder_icon = ImageTk.PhotoImage(Image.open(img_shredder))
shuttle_icon = ImageTk.PhotoImage(Image.open(img_shuttle))
smelt_icon = ImageTk.PhotoImage(Image.open(img_smelt))
soil_icon = ImageTk.PhotoImage(Image.open(img_soil))
solar_icon = ImageTk.PhotoImage(Image.open(img_solar))
tether_icon = ImageTk.PhotoImage(Image.open(img_tether))
trade_icon = ImageTk.PhotoImage(Image.open(img_trade))
vehicle_icon = ImageTk.PhotoImage(Image.open(img_vehicle))
winch_icon = ImageTk.PhotoImage(Image.open(img_winch))
wind_icon = ImageTk.PhotoImage(Image.open(img_wind))
worklight_icon = ImageTk.PhotoImage(Image.open(img_worklight))

#Raw Materials
hermatite_icon = ImageTk.PhotoImage(Image.open(img_hermatite))
wolframite_icon = ImageTk.PhotoImage(Image.open(img_wolframite))
titanite_icon = ImageTk.PhotoImage(Image.open(img_titanite))
compound_icon = ImageTk.PhotoImage(Image.open(img_comound))
resin_icon = ImageTk.PhotoImage(Image.open(img_resin))
organic_icon = ImageTk.PhotoImage(Image.open(img_organic))
clay_icon = ImageTk.PhotoImage(Image.open(img_clay))
graphite_icon = ImageTk.PhotoImage(Image.open(img_graphite))
quartz_icon = ImageTk.PhotoImage(Image.open(img_quartz))
laterite_icon = ImageTk.PhotoImage(Image.open(img_laterite))
ammonium_icon = ImageTk.PhotoImage(Image.open(img_ammonium))
astronium_icon = ImageTk.PhotoImage(Image.open(img_astronium))
sphalerite_icon = ImageTk.PhotoImage(Image.open(img_sphalerite))
malachite_icon = ImageTk.PhotoImage(Image.open(img_malachite))
lithium_icon = ImageTk.PhotoImage(Image.open(img_lithium))
#Refined items
aluminium_icon = ImageTk.PhotoImage(Image.open(img_aluminium))
carbon_icon = ImageTk.PhotoImage(Image.open(img_carbon))
ceramic_icon = ImageTk.PhotoImage(Image.open(img_ceramic))
copper_icon = ImageTk.PhotoImage(Image.open(img_copper))
glass_icon = ImageTk.PhotoImage(Image.open(img_glass))
iron_icon = ImageTk.PhotoImage(Image.open(img_iron))
titanium_icon = ImageTk.PhotoImage(Image.open(img_titanium))
tungsten_icon = ImageTk.PhotoImage(Image.open(img_tungsten))
zinc_icon = ImageTk.PhotoImage(Image.open(img_zinc))
#Composite items
aluminum_alloy_icon = ImageTk.PhotoImage(Image.open(img_aluminium_alloy))
diamond_icon = ImageTk.PhotoImage(Image.open(img_diamond))
explosive_powder_icon = ImageTk.PhotoImage(Image.open(img_explosive_powder))
hydrazine_icon = ImageTk.PhotoImage(Image.open(img_hydrazine))
nanocarbon_alloy_icon = ImageTk.PhotoImage(Image.open(img_nanocarbon_alloy))
plastic_icon = ImageTk.PhotoImage(Image.open(img_plastic))
rubber_icon = ImageTk.PhotoImage(Image.open(img_rubber))
silicone_icon = ImageTk.PhotoImage(Image.open(img_silicone))
steel_icon = ImageTk.PhotoImage(Image.open(img_steel))
titanium_alloy_icon = ImageTk.PhotoImage(Image.open(img_titanium_alloy))
tungsten_carbide_icon = ImageTk.PhotoImage(Image.open(img_tungsten_carbide))
graphene_icon = ImageTk.PhotoImage(Image.open(img_graphene))
#Gases
argon_icon = ImageTk.PhotoImage(Image.open(img_argon))
hydrogen_icon = ImageTk.PhotoImage(Image.open(img_hydrogen))
nitrogen_icon = ImageTk.PhotoImage(Image.open(img_nitrogen))
helium_icon = ImageTk.PhotoImage(Image.open(img_helium))
methane_icon = ImageTk.PhotoImage(Image.open(img_methane))
sulfur_icon = ImageTk.PhotoImage(Image.open(img_sulfur))


tk.Label(root, image=compound_icon, height=30, width=30).grid(row=2, column=0)
tk.Label(root, image=resin_icon, height=30, width=30).grid(row=3, column=0)
tk.Label(root, image=organic_icon, height=30, width=30).grid(row=4, column=0)
tk.Label(root, image=quartz_icon, height=30, width=30).grid(row=5, column=0)
tk.Label(root, image=wolframite_icon, height=30, width=30).grid(row=6, column=0)
tk.Label(root, image=clay_icon, height=30, width=30).grid(row=7, column=0)
tk.Label(root, image=hermatite_icon, height=30, width=30).grid(row=8, column=0)
tk.Label(root, image=malachite_icon, height=30, width=30).grid(row=9, column=0)
tk.Label(root, image=laterite_icon, height=30, width=30).grid(row=10, column=0)
tk.Label(root, image=ammonium_icon, height=30, width=30).grid(row=11, column=0)
tk.Label(root, image=graphite_icon, height=30, width=30).grid(row=12, column=0)
tk.Label(root, image=titanite_icon, height=30, width=30).grid(row=13, column=0)
tk.Label(root, image=lithium_icon, height=30, width=30).grid(row=14, column=0)
tk.Label(root, image=sphalerite_icon, height=30, width=30).grid(row=15, column=0)
tk.Label(root, image=astronium_icon, height=30, width=30).grid(row=16, column=0)

tk.Label(root, text="NAME").grid(row=0, column=2,)
tk.Label(root, text="------------").grid(row=1, column=2,)
tk.Label(root, text="Compound").grid(row=2, column=2)
tk.Label(root, text="Resin").grid(row=3, column=2)
tk.Label(root, text="Organic").grid(row=4, column=2)
tk.Label(root, text="Quartz").grid(row=5, column=2)
tk.Label(root, text="Wolframite").grid(row=6, column=2)
tk.Label(root, text="Clay").grid(row=7, column=2)
tk.Label(root, text="Hematite").grid(row=8, column=2)
tk.Label(root, text="Malachite").grid(row=9, column=2)
tk.Label(root, text="Laterite").grid(row=10, column=2)
tk.Label(root, text="Ammonium").grid(row=11, column=2)
tk.Label(root, text="Graphite").grid(row=12, column=2)
tk.Label(root, text="Titanite").grid(row=13, column=2)
tk.Label(root, text="Lithium").grid(row=14, column=2)
tk.Label(root, text="Sphalerite").grid(row=15, column=2)
tk.Label(root, text="Astronium").grid(row=16, column=2)

tk.Label(root, text="-").grid(row=2, column=3)
tk.Label(root, text="-").grid(row=3, column=3)
tk.Label(root, text="-").grid(row=4, column=3)
tk.Label(root, text="-").grid(row=5, column=3)
tk.Label(root, text="-").grid(row=6, column=3)
tk.Label(root, text="-").grid(row=7, column=3)
tk.Label(root, text="-").grid(row=8, column=3)
tk.Label(root, text="-").grid(row=9, column=3)
tk.Label(root, text="-").grid(row=10, column=3)
tk.Label(root, text="-").grid(row=11, column=3)
tk.Label(root, text="-").grid(row=12, column=3)
tk.Label(root, text="-").grid(row=13, column=3)
tk.Label(root, text="-").grid(row=14, column=3)
tk.Label(root, text="-").grid(row=15, column=3)
tk.Label(root, text="-").grid(row=16, column=3)

tk.Label(root, text="SMELTING").grid(row=0, column=4,)
tk.Label(root, text="------------").grid(row=1, column=4,)
tk.Label(root, text="n/a").grid(row=2, column=4)
tk.Label(root, text="n/a").grid(row=3, column=4)
tk.Label(root, text="Carbon").grid(row=4, column=4)
tk.Label(root, text="Glass").grid(row=5, column=4)
tk.Label(root, text="Tungsten").grid(row=6, column=4)
tk.Label(root, text="Ceramic").grid(row=7, column=4)
tk.Label(root, text="Iron").grid(row=8, column=4)
tk.Label(root, text="Copper").grid(row=9, column=4)
tk.Label(root, text="Aluminum").grid(row=10, column=4)
tk.Label(root, text="n/a").grid(row=11, column=4)
tk.Label(root, text="n/a").grid(row=12, column=4)
tk.Label(root, text="Titanium").grid(row=13, column=4)
tk.Label(root, text="n/a").grid(row=14, column=4)
tk.Label(root, text="Zinc").grid(row=15, column=4)
tk.Label(root, text="n/a").grid(row=16, column=4)

tk.Label(root, image="").grid(row=2, column=5)
tk.Label(root, image=carbon_icon, height=30, width=30).grid(row=4, column=5)
tk.Label(root, image=glass_icon, height=30, width=30).grid(row=5, column=5)
tk.Label(root, image=tungsten_icon, height=30, width=30).grid(row=6, column=5)
tk.Label(root, image=ceramic_icon, height=30, width=30).grid(row=7, column=5)
tk.Label(root, image=iron_icon, height=30, width=30).grid(row=8, column=5)
tk.Label(root, image=copper_icon, height=30, width=30).grid(row=9, column=5)
tk.Label(root, image=aluminium_icon, height=30, width=30).grid(row=10, column=5)
tk.Label(root, image=titanium_icon, height=30, width=30).grid(row=13, column=5)
tk.Label(root, image=zinc_icon, height=30, width=30).grid(row=15, column=5)

tk.Label(root, text="ATH. CON").grid(row=0, column=7)
tk.Label(root, text="------------").grid(row=1, column=7)
tk.Label(root, image=methane_icon, height=30, width=30).grid(row=2, column=7)
tk.Label(root, image=sulfur_icon, height=30, width=30).grid(row=3, column=7)
tk.Label(root, image=argon_icon, height=30, width=30).grid(row=4, column=7)
tk.Label(root, image=hydrogen_icon, height=30, width=30).grid(row=5, column=7)
tk.Label(root, image=nitrogen_icon, height=30, width=30).grid(row=6, column=7)
tk.Label(root, image=helium_icon, height=30, width=30).grid(row=7, column=7)

tk.Label(root, text="Methane").grid(row=2, column=8)
tk.Label(root, text="Sulfur").grid(row=3, column=8)
tk.Label(root, text="Argon").grid(row=4, column=8)
tk.Label(root, text="Hydrogen").grid(row=5, column=8)
tk.Label(root, text="Nitrogen").grid(row=6, column=8)
tk.Label(root, text="Helium").grid(row=7, column=8)

tk.Label(root, text="CHEM LAB").grid(row=0, column=9)
tk.Label(root, text="------------").grid(row=1, column=9)
tk.Label(root, text="Silicone").grid(row=2, column=9)
tk.Label(root, text="Rubber").grid(row=3, column=9)
tk.Label(root, text="Plastic").grid(row=4, column=9)
tk.Label(root, text="Explosive Powder").grid(row=5, column=9)
tk.Label(root, text="Steel").grid(row=6, column=9)
tk.Label(root, text="Tungsten Carbide").grid(row=7, column=9)
tk.Label(root, text="Aluminum Alloy").grid(row=8, column=9)
tk.Label(root, text="Hydrazine").grid(row=9, column=9)
tk.Label(root, text="Diamond").grid(row=10, column=9)
tk.Label(root, text="Graphene").grid(row=11, column=9)
tk.Label(root, text="Titanium Alloy").grid(row=12, column=9)
tk.Label(root, text="Nanocarbon Alloy").grid(row=13, column=9)

tk.Label(root, image=silicone_icon).grid(row=2, column=10)
tk.Label(root, image=rubber_icon).grid(row=3, column=10)
tk.Label(root, image=plastic_icon).grid(row=4, column=10)
tk.Label(root, image=explosive_powder_icon).grid(row=5, column=10)
tk.Label(root, image=steel_icon).grid(row=6, column=10)
tk.Label(root, image=tungsten_carbide_icon).grid(row=7, column=10)
tk.Label(root, image=aluminum_alloy_icon).grid(row=8, column=10)
tk.Label(root, image=hydrazine_icon).grid(row=9, column=10)
tk.Label(root, image=diamond_icon).grid(row=10, column=10)
tk.Label(root, image=graphene_icon).grid(row=11, column=10)
tk.Label(root, image=titanium_alloy_icon).grid(row=12, column=10)
tk.Label(root, image=nanocarbon_alloy_icon).grid(row=13, column=10)

tk.Label(root, image=silicon_rec).grid(row=2, column=11)
tk.Label(root, image=rubber_rec).grid(row=3, column=11)
tk.Label(root, image=plastic_rec).grid(row=4, column=11)
tk.Label(root, image=explosive_powder_rec).grid(row=5, column=11)
tk.Label(root, image=steel_rec).grid(row=6, column=11)
tk.Label(root, image=tungsten_carbide_rec).grid(row=7, column=11)
tk.Label(root, image=aluminum_alloy_rec).grid(row=8, column=11)
tk.Label(root, image=hydrazine_rec).grid(row=9, column=11)
tk.Label(root, image=diamond_rec).grid(row=10, column=11)
tk.Label(root, image=graphene_rec).grid(row=11, column=11)
tk.Label(root, image=titanium_alloy_rec).grid(row=12, column=11)
tk.Label(root, image=nanocarbon_alloy_rec).grid(row=13, column=11)

root.mainloop()
