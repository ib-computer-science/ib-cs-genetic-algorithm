// Figure 3: Types of crossover
// Two panels: "One-point crossover" and "Two-point crossover".
// Each panel shows, top to bottom:
//   - two parent chromosomes (straight horizontal bars)
//   - the two parents crossing over (one crossing for one-point,
//     two crossings for two-point)
//   - the two reciprocal offspring that result (each a recombination
//     of the two parent segments)

size(360, 230, IgnoreAspect);

real panelWidth = 1.2;
real lineThick = 2.5;

// ---- One-point crossover (left panel) ----
void onePointPanel(real ox) {
    real y0a = 3.3;  // parent row (top line)
    real y0b = 3.0;  // parent row (second line)
    real y1  = 1.6;  // crossing row (centreline)
    real y2a = 0.3;  // offspring row 1
    real y2b = 0.0;  // offspring row 2
    real xL = ox, xR = ox + panelWidth;
    real xm = ox + panelWidth * 0.5; // single crossover point

    // parent lines: gray on top, black below (matches the source figure)
    draw((xL, y0a) -- (xR, y0a), gray(0.55) + linewidth(lineThick));
    draw((xL, y0b) -- (xR, y0b), black + linewidth(lineThick));

    // crossing strands: simple straight lines, exactly one crossing
    draw((xL, y1 + 0.15) -- (xR, y1 - 0.15), black + linewidth(lineThick));
    draw((xL, y1 - 0.15) -- (xR, y1 + 0.15), gray(0.55) + linewidth(lineThick));

    // offspring 1: black head + gray tail
    draw((xL, y2a) -- (xm, y2a), black + linewidth(lineThick));
    draw((xm, y2a) -- (xR, y2a), gray(0.55) + linewidth(lineThick));

    // offspring 2 (reciprocal): gray head + black tail
    draw((xL, y2b) -- (xm, y2b), gray(0.55) + linewidth(lineThick));
    draw((xm, y2b) -- (xR, y2b), black + linewidth(lineThick));

    label("One-point crossover", (ox + panelWidth / 2, y0a + 0.5), fontsize(9pt));
}

// ---- Two-point crossover (right panel) ----
void twoPointPanel(real ox) {
    real y0a = 3.3;  // parent row (top line, black)
    real y0b = 3.0;  // parent row (second line, gray)
    real y1  = 1.6;  // crossing row (centreline)
    real y2a = 0.3;  // offspring row 1
    real y2b = 0.0;  // offspring row 2
    real xL = ox, xR = ox + panelWidth;
    real xm1 = ox + panelWidth * 0.2;
    real xm2 = ox + panelWidth * 0.8;
    real xmid = (xm1 + xm2) / 2;

    // parent lines: black on top, gray below
    draw((xL, y0a) -- (xR, y0a), black + linewidth(lineThick));
    draw((xL, y0b) -- (xR, y0b), gray(0.55) + linewidth(lineThick));

    // crossing strands: two crossings (at xm1 and xm2), forming a lens;
    // both strands start and end on their original (top/bottom) side
    draw((xL, y1 + 0.15) .. (xm1, y1) .. (xmid, y1 - 0.3) .. (xm2, y1) .. (xR, y1 + 0.15),
         black + linewidth(lineThick));
    draw((xL, y1 - 0.15) .. (xm1, y1) .. (xmid, y1 + 0.3) .. (xm2, y1) .. (xR, y1 - 0.15),
         gray(0.55) + linewidth(lineThick));

    // offspring 1: black - gray - black
    draw((xL, y2a) -- (xm1, y2a), black + linewidth(lineThick));
    draw((xm1, y2a) -- (xm2, y2a), gray(0.55) + linewidth(lineThick));
    draw((xm2, y2a) -- (xR, y2a), black + linewidth(lineThick));

    // offspring 2 (reciprocal): gray - black - gray
    draw((xL, y2b) -- (xm1, y2b), gray(0.55) + linewidth(lineThick));
    draw((xm1, y2b) -- (xm2, y2b), black + linewidth(lineThick));
    draw((xm2, y2b) -- (xR, y2b), gray(0.55) + linewidth(lineThick));

    label("Two-point crossover", (ox + panelWidth / 2, y0a + 0.5), fontsize(9pt));
}

onePointPanel(0);
twoPointPanel(panelWidth + 0.6);

// downward arrow at the left, showing the flow from parents to offspring
draw((-0.4, 3.3) -- (-0.4, 0.0), gray(0.4) + linewidth(1.5), Arrow(size=10));
