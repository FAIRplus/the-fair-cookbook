import pathlib
import copy

#all_md_files = list(pathlib.Path("../content").glob("**/*.md"))[:25]
all_md_files = [pathlib.Path("../content/recipes/introduction/the-turing-way.md")]
#all_md_files = [pathlib.Path("../content/recipes/findability/seo/bioschemas-datacatalog.md")]
print(len(all_md_files))

for file in all_md_files:
    content = file.read_text()
    original_content = copy.copy(content)
    #
    start_position = 0
    offset = 0
    while True:
        #print("while True")
        contains_figure_directive_at_position = content.find("{figure}", start_position)
        if contains_figure_directive_at_position == -1:
            break 
        contains_figure_directive_at_line = original_content.count("\n", 0, contains_figure_directive_at_position+offset) +1
        filel = file.as_posix() + f":{contains_figure_directive_at_line}"
        #print(contains_figure_directive_at_position)
        #
        directive_start_at_position = content.find("```", contains_figure_directive_at_position-10)
        if directive_start_at_position == -1:
            raise 
        directive_end_at_position = content.find("```", contains_figure_directive_at_position)
        #
        directive_original_content = content[directive_start_at_position:directive_end_at_position+3]
        directive_lines = directive_original_content.splitlines()
        #
        error = 0
        if not directive_lines[0].startswith("```{figure} "):
            print(filel, "ERROR: unusual line:", directive_lines[0])
            error += 1
        if not directive_lines[1] == "---":
            print(filel, "ERROR: unusual line:", directive_lines[1])
            error += 1
        if not directive_lines[-1] == "```":
            print(filel, "ERROR: unusual line:", directive_lines[-1])
            error += 1
        if directive_lines[2].startswith("height: "):
            null = directive_lines.pop(2)
        if directive_lines[2].startswith("width: "):
            null = directive_lines.pop(2)
        if directive_lines[2].startswith("height: "):
            null = directive_lines.pop(2)
        if not directive_lines[2].startswith("name: "):
            print(filel, "ERROR: unusual line:", directive_lines[2])
            error += 1
        if not directive_lines[3].startswith("alt: "):
            print(filel, "ERROR: unusual line:", directive_lines[3])
            error += 1
        if not directive_lines[4] == "---":
            print(filel, "ERROR: unusual line:", directive_lines[4])
            error += 1
        if not directive_lines[6] == "```":
            print(filel, "ERROR: unusual line:", directive_lines[6])
            error += 1
        #
        name_of_figure = None
        subtitle = None
        if directive_lines[2].replace("name: ", "").strip() == directive_lines[3].replace("alt: ", "").strip():
            #print(filel, "TODO: please correct naming:", repr(directive_lines[2]) )
            name_of_figure = "TODO"
        elif directive_lines[2].replace("name: ", "").strip() in directive_lines[5]:
            #print(filel, "TODO: correct naming:", repr(directive_lines[1]) )
            directive_lines[3] = directive_lines[3].replace("alt: ", "alt: "+directive_lines[2].replace("name: ", "").strip()+" ")
            name_of_figure = "TODO"
        elif " " in directive_lines[2].replace("name: ", "").strip():
            print(filel, "ERROR: invalid name:", directive_lines[2])
            error += 1
        else:
            name_of_figure = directive_lines[2].replace("name: ", "").strip()
        subtitle       = directive_lines[3].replace("alt: " , "").strip()
        #
        if subtitle in directive_lines[5]:
            subtitle = directive_lines[5]
        else:
            print(filel, "ERROR: need to correct alt / subtitle:", repr(directive_lines[3]), repr(directive_lines[5]) )
            error += 1
        #
        if error > 0:
            start_position = directive_end_at_position
            continue
        #
        directive_lines[0] = directive_lines[0].replace("{figure}", "{figure_fairplus}")
        directive_lines[0] = directive_lines[0].replace(".mmd.png", ".mmd")
        del(directive_lines[1:])        
        directive_lines.append("name: " + name_of_figure)
        directive_lines.append("subtitle: " + subtitle)
        directive_lines.append("```")
        
        new_content = "\n".join(directive_lines)
        #
        print(filel, f"replacing from {directive_start_at_position}")
        print(new_content)
        print("")
        content = content.replace(directive_original_content, new_content, 1)
        file.write_text(content)
        offset += len(directive_original_content)-len(new_content) 
        pass
    #   
    #print(filel)
    #print(directive_original_content)

