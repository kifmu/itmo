package special_moves;

import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class AncientPower extends SpecialMove{
    public AncientPower(){
        super(Type.ROCK, 60, 100);
    }
    private int isCorrectnum = 0;
    @Override
    public void applySelfEffects(Pokemon pokemon) {
        if (Math.random() <= 1.0 && isCorrectnum <= 6) {
            pokemon.setMod(Stat.ATTACK, 1);
            pokemon.setMod(Stat.DEFENSE, 1);
            pokemon.setMod(Stat.SPECIAL_ATTACK, 1);
            pokemon.setMod(Stat.SPECIAL_DEFENSE, 1);
            pokemon.setMod(Stat.SPEED, 1);
            isCorrectnum += 1;
        }
    }

    @Override
    protected String describe() {
        return "использует Ancient Power";
    }
}