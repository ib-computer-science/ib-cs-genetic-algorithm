// Figure 2: Computer-generated image using the data in Figure 1
// to show the location of the cities Lotte wants to visit

size(300, 260, IgnoreAspect);
import graph;
import markers;

// approximate (x, y) coordinates read off the scatter plot, in km
pair[] pts = {
    (140,  90), // X
    (230,  78), // A
    (100, 157), // B
    ( 20, 165), // C
    (195,  20), // D
    (130,  32), // E
    (225, 182), // F
    (260,  13), // G
    (225, 111), // H
    ( 90,  42), // I
    (125,   3), // J
    (195, 112), // K
    (  5,  54), // L
    (255,  97), // M
    (175,  60), // N
    (100, 119), // O
    (150,  88), // P
    ( 15,  10), // Q
    (150, 160), // R
    (225,  18), // S
    (125,  75)  // T
};

string[] labels = {
    "X", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"
};

for (int i = 0; i < pts.length; ++i) {
    dot(pts[i], black + linewidth(3));
    label(labels[i], pts[i], NE, fontsize(8pt));
}

xaxis("Kilometres (km)", BottomTop, LeftTicks);
yaxis("Kilometres (km)", LeftRight, RightTicks);
