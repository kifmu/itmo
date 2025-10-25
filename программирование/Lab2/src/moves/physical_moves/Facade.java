package physical_moves;

import ru.ifmo.se.pokemon.*;

public class Facade extends PhysicalMove {
    public Facade() {
        super(Type.NORMAL,70, 100);
    }
    private boolean hasStatus(Pokemon pokemon) {
        Status condition = pokemon.getCondition();
        return condition == Status.BURN || 
               condition == Status.POISON || 
               condition == Status.PARALYZE;
    }
     @Override
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        if (hasStatus(att)) {
            double originalPower = this.power;
            this.power = 140;
            double damage = super.calcBaseDamage(att, def);
            this.power = originalPower;
            return damage;
        } else {
            return super.calcBaseDamage(att, def);
        }
    }
    @Override
    protected String describe() {
        return "использует Facade";
    }
}
