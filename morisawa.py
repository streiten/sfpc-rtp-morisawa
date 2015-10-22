# Open the svg template
f_tpl = open("master.tpl.svg", 'r')
svg_tpl = f_tpl.read()
f_tpl.close()

#generat the elements
symbol_width = 650.0
symbol_height = 142.0

poster_width = 650
poster_height = 911

svg_elems = ''
y_val = 0.0
i = 0

while poster_height > y_val:
    width = symbol_width / (i+1)
    x_val = 0
    scale = 1.0 / (i+1)

    # print str(i) + ':' + str(width) + ' - scale: ' + str(scale)

    for j in range(i+1):
        # building the actual element
        svg_elems += '<use xlink:href="#morisawa-logo" x="0" y="0" transform="translate(' + str(x_val) + ' ' + str(y_val) +') scale('+str(scale)+' '+str(scale)+')" />\n'
        x_val += width

    y_val += symbol_height / (i+1)
    i += 1
    # print '---'

print y_val
print i


# assemble the svg chunks
svg_chunks = svg_tpl.split('<!-- @@ -->')
svg_chunks.insert(1, svg_elems)
final_svg = '\n'.join(svg_chunks)

# write out the final file
f_out = open("master.svg", 'w')
f_out.write(final_svg)
f_out.close()
