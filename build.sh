
cd java/src;
javac Calculator.java Main.java;
jar cfm MyProject.jar Manifest.txt Calculator.class Main.class;
echo "Built successfully!";
#