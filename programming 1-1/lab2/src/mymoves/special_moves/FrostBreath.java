package special_moves;

import ru.ifmo.se.pokemon.*;

public class FrostBreath extends SpecialMove {

    public FrostBreath() {
        super(Type.ICE, 60, 90);
    }
    @Override
    protected double calcCriticalHit(Pokemon att, Pokemon def) {
        return 1.0;
       
    }
    @Override
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        double originalPower = this.power;
        this.power = 90;
        double damage = super.calcBaseDamage(att, def);
        this.power = originalPower;
        return damage;
    }
    protected String describe(){
        return "использует Frost Breath";

    }
}
