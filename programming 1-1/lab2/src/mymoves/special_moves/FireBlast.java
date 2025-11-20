package special_moves;

import ru.ifmo.se.pokemon.*;

public class FireBlast extends SpecialMove{
    public FireBlast() {
        super(Type.FIRE,110,85);
    }
    boolean isBurned = false;
    @Override
    public void applyOppEffects(Pokemon pokemon) {
        if (Math.random() <= 0.1) {
            Effect.burn(pokemon);
            isBurned = true;
        }
    }
    @Override
    protected String describe() {
        return ("использует Fire Blast" + ((isBurned) ? "и burn цель" : ""));
    }

}
