import pathlib
import copy

all_md_files = list(pathlib.Path("../content").glob("**/*.md")) #[:25]
#all_md_files = [pathlib.Path("../content/recipes/introduction/the-turing-way.md")]
#all_md_files = [pathlib.Path("../content/recipes/findability/seo/bioschemas-datacatalog.md")]
#all_md_files = [pathlib.Path("../content/recipes/interoperability/bridgedb-recipe.md")]
print(len(all_md_files))

for file in all_md_files:

    if "help/myst.md" in file.as_posix():
        continue

    print()
    print(f"Acting on file {file} ...")
    content = file.read_text()
    original_content = copy.copy(content)
    #
    start_position = 0
    offset = 0
    replacements_made = 0
    while True:
        #print("while True")
        contains_figure_directive_at_position = content.find("{figure}", start_position)
        if contains_figure_directive_at_position == -1:
            break 
        contains_figure_directive_at_line = original_content.count("\n", 0, contains_figure_directive_at_position+offset) +1
        filel = file.as_posix() + f":{contains_figure_directive_at_line}"
        print()
        print(f"... acting on directive at {filel} :")
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
            print("   ", "ERROR: unusual line:", directive_lines[0])
            error += 1
        if not directive_lines[1] == "---":
            print("   ", "ERROR: unusual line:", directive_lines[1])
            error += 1
        if not directive_lines[-1] == "```":
            print("   ", "ERROR: unusual line:", directive_lines[-1])
            error += 1

        ## workaround 
        if directive_lines[-1] == "```" and directive_lines[-3] == "---":
            print("   ", f"DEBUG: assuming this is a text line: {directive_lines[-2]}")
            directive_lines[-2] = "text: " + directive_lines[-2]
        
        linedict = {}
        for counter, line in enumerate(directive_lines):
            index = line.find(":")
            
            if line.strip() == "---":
                continue 
            elif line.strip() == "```":
                continue 
            elif line.strip().startswith("```{figure} "):
                continue 

            if index == -1:
                print("   ", "ERROR: unusual line:", line)
                error += 1
                continue 
        
            a,b = line[:index], line[index+1:]
            key = a.strip()
            value = b.strip()

            if key in linedict:
                print("   ", "ERROR: got the same key twice:", key)
                error += 1
                continue 
            
            linedict.update({key: value})
        
        ## remove undesired values
        linedict.pop("height", None)
        linedict.pop("width", None)

        #
        print("   ", f"{linedict=}")
        name_of_figure = None
        subtitle = None

        if "name" not in linedict:
            print("   ", "WARNING: I didn't find a name line in this directive")
            error += 1
        if "alt" not in linedict:
            print("   ", "WARNING: I didn't find a alt line in this directive")
            error += 1
        if "text" not in linedict:
            print("   ", "WARNING: I didn't find a text line in this directive")
            error += 1


        if linedict.get("name", None) == linedict.get("alt", None):
            #print("   ", "DEBUG: you will need to correct the naming of this figure, as I will replace the name with 'TODO'...")
            name_of_figure = "TODO"
        elif linedict.get("name", "") in linedict.get("alt", ""):
            print("   ", "DEBUG: strange case here about name and alt lines:", repr((linedict.get("name", ""), linedict.get("alt", ""))) )
            #print("   ", "DEBUG: you will need to correct the naming of this figure, as I will replace the name with 'TODO'...")
            name_of_figure = "TODO"
        
        if " " in linedict.get("name", ""):
            print("   ", "ERROR: invalid name:", repr(linedict.get("name", "")))
            error += 1


        name_of_figure = linedict.get("name", "").strip()
        subtitle       = linedict.get("alt", "").strip()

        if linedict.get("alt").strip() in linedict.get("text").strip():
            subtitle = linedict.get("text", "").strip()
        else:
            print("   ", "ERROR: you need to correct alt / subtitle manually:", repr(directive_lines[3]), repr(directive_lines[5]) )
            error += 1

        #
        if error > 0:
            print("   ", "... not doing anything because of previous errors.")
            start_position = directive_end_at_position
            continue
        #
        print("   ", "... starting automated replacement ...")
        directive_lines[0] = directive_lines[0].replace("{figure}", "{figure_fairplus}")
        directive_lines[0] = directive_lines[0].replace(".mmd.png", ".mmd")
        del(directive_lines[1:])        
        directive_lines.append("name: " + name_of_figure)
        directive_lines.append("subtitle: " + subtitle)
        directive_lines.append("```")
        
        new_content = "\n".join(directive_lines)
        #
        #print("   ", f"replacing from {directive_start_at_position}")
        #print(new_content)
        #print("")
        content = content.replace(directive_original_content, new_content, 1)
        file.write_text(content)
        offset += len(directive_original_content)-len(new_content) 
        
        replacements_made += 1
        print("   ", "... done.")
    
    if replacements_made == 0:
        print("   ", "no replacements made.")
        continue 
    else:
        pass
        #break
    #   
    #print(filel)
    #print(directive_original_content)

print("...done.")