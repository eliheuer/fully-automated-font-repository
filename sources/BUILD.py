import argparse
import os
import subprocess
from fontTools.ttLib import TTFont


# FONTMAKE
try:
    print("\n**** Running Fontmake ******************************")
    print("     [+] Run: fontmake -g sources/Foo.glyphs -o variable")
    subprocess.call(['fontmake', '-g', 'sources/Foo.glyphs', '-o', 'variable',])
    print("     [+] Done")
except:
    print("Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")


# MOVE FONTS
print("\n**** Moving fonts to fonts directory *******************")
subprocess.call(['cp', 'variable_ttf/Foo-VF.ttf', 'fonts/',])
print("     [+] Done")


# CLEANUP
print("\n**** Removing build directories  ***********************")
print("     [+] Run: rm -rf variable_ttf master_ufo")
subprocess.call(['rm', '-rf', 'variable_ttf', 'master_ufo'])
print("     [+] Done")


# AUTOHINT
print("\n**** Run: ttfautohint  *********************************")
os.chdir('fonts')
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
subprocess.call(['ttfautohint', '-I', 'Foo-VF.ttf', 'Foo-VF-Fix.ttf'])
subprocess.call(['cp', 'Foo-VF-Fix.ttf', 'Foo-VF.ttf'])
subprocess.call(['rm', '-rf', 'Foo-VF-Fix.ttf'])
print("     [+] Done")


# GFTOOLS
print("\n**** Run: gftools  **************************************\n")
os.chdir("..")
cwd = os.getcwd()
print("     [+]In Directory:", cwd)
#subprocess.call(['gftools fix-dsgi', 'fonts/Foo-VF.ttf', '--autofix'])


# FONTTOOLS
print("\n**** Run: edit xAvgCharWidth  *********************************\n")
cwd = os.getcwd()
print("     In Directory:", cwd)
font = TTFont('fonts/Foo-VF.ttf')
print(font)
print("     [+] Done")

subprocess.call('python3 docs/drawbot-sources/basic-specimen.py', shell=True)
