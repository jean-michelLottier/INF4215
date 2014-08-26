(define (problem two-jugs)
	(:domain jug-pouring)

	(:objects jug1 jug2)

	(:init
	  (= (capacity jug1) 3)
	  (= (capacity jug2) 4)
	  (= (amount jug1) 0)
	  (= (amount jug2) 0))


        (:goal (exists (?x) (= (amount ?x) 2))))

