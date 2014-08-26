(define (domain store)
     (:constants myAgent)
     
     (:functions 
         (packageWeight ?p)
         (agentLoadWeight ?a)
         (agentMaxLoad ?a)
         (distance ?x ?y)
         (cost))


     (:predicates
         (package ?p)
		 (packageAt ?p ?n)
		 (packageDest ?p ?n)
         (node ?n)
         (agent ?a)
		 (agentAt ?a ?n)
         (connected ?x ?y)
         (in ?p ?a)
         (delivered ?p))

     (:action take
         :parameters (?pkg ?pos)
         :precondition (and (package ?pkg)
                            (node ?pos)
                            (not (delivered ?pkg))
                            (packageAt ?pkg ?pos)
		                    (agentAt myAgent ?pos)
		                    (not (in ?pkg myAgent))
                            (<= (+ (packageWeight ?pkg) (agentLoadWeight myAgent)) (agentMaxLoad myAgent))
                            (not (packageDest ?pkg ?pos)))
         :effect (and (in ?pkg myAgent)
                      (increase (agentLoadWeight myAgent) (packageWeight ?pkg))
                      (not (packageAt ?pkg ?pos))))

	 (:action move
         :parameters (?from ?to)
		 :precondition (and (node ?from)
                            (node ?to)
                            (agentAt myAgent ?from)
                            (not (agentAt myAgent ?to)))
         :effect (and (increase (cost) (distance ?from ?to))
					  (agentAt myAgent ?to)
                      (not (agentAt myAgent ?from))))		  
					  
     (:action drop
	     :parameters (?pkg ?pos)
	     :precondition (and (package ?pkg)
                            (node ?pos)
		                    (agentAt myAgent ?pos)
	                        (in ?pkg myAgent) 
	                        (packageDest ?pkg ?pos))
	     :effect (and (not (in ?pkg myAgent))
	                  (decrease (agentLoadWeight myAgent) (packageWeight ?pkg))
	                  (delivered ?pkg)
                      (packageAt ?pkg ?pos))))
