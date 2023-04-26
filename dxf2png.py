import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

ezdxf.options.check_entity_tag_structures = False
filename = "ZG20180817"
doc = ezdxf.readfile("C:\\Users\\fashu\\Documents\\ezdxf\\" + filename +".dxf")
msp = doc.modelspace()

if 'building' not in doc.layers:
    print("there is no building layer in " + filename)
    exit()

for layer in doc.layers:
    layer.rgb = (255,255,255) #turn all objects white
# for e in msp:
#     e.rgb=(0,0,0)


# buildings = msp.query('LINE[layer=="Building"]')
# sites = msp.query('*[layer=="SITE"]')

lines = msp.query('* !HATCH[layer=="building"]')
for l in lines:
     msp.delete_entity(l)
# Recommended: audit & repair DXF document before rendering
auditor = doc.audit()
# The auditor.errors attribute stores severe errors,
# which *may* raise exceptions when rendering.

for layer in doc.layers:
    if layer.dxf.name != 'Building' and layer.dxf.name != 'building':
        print(layer.dxf.name)
        layer.off()


# hatch = msp.add_hatch(color=7)
# site_layer=doc.layers.get('SITE')
# edge_path = hatch.paths.add_edge_path()
# for line in sites:
#     edge_path.add_line(line.dxf.start,line.dxf.end)

if len(auditor.errors) == 0:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(msp, finalize=True)
    fig.savefig(filename+'_building.png', dpi=300, transparent=True)


doc = ezdxf.readfile("C:\\Users\\fashu\\Documents\\ezdxf\\" + filename +".dxf")

msp = doc.modelspace()
for layer in doc.layers:
        layer.rgb = (0, 0, 0)  # turn all objects black
hatches = msp.query('HATCH')
for h in hatches:
     msp.delete_entity(h)
auditor = doc.audit()
if len(auditor.errors) == 0:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(msp, finalize=True)
    fig.savefig(filename+'.png', dpi=300, transparent=True)


