package special_moves;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;
import ru.ifmo.se.pokemon.Pokemon;

public class Hurricane extends SpecialMove {
        public Hurricane() {
                super(Type.FLYING, 110, 70);
                    }

        private boolean isConfused = false;
        @Override
        public void applyOppEffects(Pokemon p) {
                if (Math.random() <= 0.3) {
                        Effect.confuse(p);
                        isConfused = true;
                }
        }
        @Override
        protected String describe(){
                return "использует Hurricane " + ((isConfused) ? "и confuse цель" : "");
                }
        
}
