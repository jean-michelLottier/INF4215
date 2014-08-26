(define (domain jug-pouring)
    (:functions
       (amount ?j)
       (capacity ?j))

    (:action fill
       :parameters (?jug)
       :effect (assign (amount ?jug) (capacity ?jug)))

    (:action empty
       :parameters (?jug)
       :effect (assign (amount ?jug) 0))


    (:action pour-all
       :parameters (?jug1 ?jug2)
       :precondition (and (<= (amount ?jug2) (capacity ?jug2))
       		     	  (<= (amount ?jug1) (- (capacity ?jug2) (amount ?jug2))))
       :effect (and (assign (amount ?jug1) 0)
                    (increase (amount ?jug2) (amount ?jug1))))

    (:action pour-partial
       :parameters (?jug1 ?jug2)
       :precondition (and (<= (amount ?jug2) (capacity ?jug2))
       		     	  (> (amount ?jug1) (- (capacity ?jug2) (amount ?jug2))))
       :effect (and (assign (amount ?jug2) (capacity ?jug2))
                    (decrease (amount ?jug1) (- (capacity ?jug2) (amount ?jug2))))))
