using System;

namespace BattleGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Warrior dhanu = new Warrior("dhanu", 1000, 120, 40);
            Warrior venky = new Warrior("venky", 1000, 120, 40);
            Battle.StartFight(dhanu, venky);
            
            Console.ReadLine();
        }
    }
    class Warrior
    {
        public string Name { get; set; }
        public double Health { get; set; }
        public double AttackMax { get; set; }
        public double BlockMax { get; set; }

        Random rand = new Random();
        public Warrior(string name, double health, double attackMax, double blockMax)
        {
            Name = name;
            Health = health;
            AttackMax = attackMax;
            BlockMax = blockMax;
        }

        public double Attack() => rand.Next(1, (int)AttackMax);
        public double Block() => rand.Next(1, (int)BlockMax);

    }
    class Battle
    {
        public static void StartFight(Warrior warrior1, Warrior warrior2)
        {
            while (true)
            {
                if (GetAttackResult(warrior1, warrior2) == "Game Over")
                {
                    Console.WriteLine("Game Over");
                    break;
                }
                if ( GetAttackResult(warrior2,warrior1 ) == "Game Over")
                {
                    Console.WriteLine("Game Over");
                    break;
                }
            }
        }
        public static string GetAttackResult(Warrior warriorA, Warrior warriorB)
        {
            double warAAttcAmount = warriorA.Attack();
            double warBBlockAmount = warriorB.Block();
            double diff = warAAttcAmount - warBBlockAmount;
            if (diff > 0)
            {
                warriorB.Health = warriorB.Health - diff;
            }
            else
            {
                diff = 0;
            }
            Console.WriteLine("{0} Attcacks {1} and deals {2} damage", warriorA.Name, warriorB.Name, diff);
            if(warriorB.Health <= 0)
            {
                Console.WriteLine("{0} has Died and {1} is victorious.", warriorB.Name, warriorA.Name);
                return "Game Over";
            }
            else
            {
                return "Fight Agagin";
            }
        }

    }
}
