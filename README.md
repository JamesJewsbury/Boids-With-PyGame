# Boids With PyGame
![Photo by <a href="https://unsplash.com/@tumbao1949?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">James Wainscoat</a> on <a href="https://unsplash.com/photos/a-large-flock-of-birds-flying-over-a-field-b7MZ6iGIoSI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>](https://github.com/JamesJewsbury/Boids-With-PyGame/blob/main/Assets/Images/Flock%20of%20Birds.jpg)
> Photo by <a href="https://unsplash.com/@tumbao1949?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">James Wainscoat</a> on <a href="https://unsplash.com/photos/a-large-flock-of-birds-flying-over-a-field-b7MZ6iGIoSI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
    
## Outline
In this project, I will be using basic Python libraries and PyGame to replicate 'boids' as detailed by Craig Reynolds in his 1987 publication "Flocks, Herds, and Schools: A Distributed Behaviour Model" [^1].

In short, Reynolds showed that the complex and fluid movements exhibited by flocks of birds or schools of fish, can be attributed to simple decisions being made by each individual being. Reynolds created 3 simple rules that controlled these agents:
1. **Flock Centering**: Boids aim to stay near the centre of the N other nearby boids.
2. **Collision Avoidance**: Just as a bird would not want to collide with it's flock-mate, neither would these boids.
3. **Velocity Matching**: Boids try to "keep-up" with one another (speed) and have a similar direction. 


## PseudoCode and Applying Reynolds' Rules
To apply these rules to code, we will being using a modified version of the PseudoCode created by Conrad Parker (2007) [^2].

### Rule 1- Flock Centering
Rule 1 works by creating an average position of all other or nearby (more on that later) boids. It then calculates the displacement needed to move the current boid to this average position. This displacement is then multiplied by a modifier in this case 0.01 which determines its influence to make sure that it does not negate the impact of the other rules.

```pseudo
FUNCTION Rule1(boid bs):
    Vector position_total
    Vector position_avg
    Vector Velocity_modifier
    
    FOR EACH BOID b
        if b != bs
            position_total+=b.positiom
        END IF
    END
    position_avg= position_total/(Boid_Count-1)
    Velocity_modifier=(position_avg-b.position)*0.01 
    
```

### Rule 2- Collision Avoidance
Boids avoid one another by calculating their proximities to each other. If a boid is within less than 100 units range, the needed velocity to move away from that boid is added to the total returned velocity. 
```pseudo
FUNCTION Rule2(boid bs):
    Vector Velocity

    FOR EACH BOID B
        if b != bs
            IF |b.position-bs.position|<100
                c-=(b.position-bs.position)
            END IF
        END IF
    END

    RETURN Velocity
```
As you can see, there is no influence modifier applied. This is as the boids HAVE to move away from each other.

### Rule 3
This rule is similar to rule 1 in functionality and implementation. Instead of averaging the positions of nearby boids, we are averaging the velocities. Again, we have an influence modifier, this time of 0.125 to start.
```pseudo
FUNCTION Rule3(boid bs):
    Vector Velocity

    FOR EACH BOID b:
        IF b!=bs
            Velocity+=b.velocity
        END IF
    END
    Velocity=Velocity/(Boid_Count-1)
    Velocity*=0.125
    RETURN Velocity
```

### Calculate New Positions
Finally, to incorporate these new rules into visible movements, we use the following simple function. In this function, we iterate through each boid and update their velocity with the new rules. We then update the position with this new modified velocity.
```pseudo
FUNCTION Calculate_New_Positions()
    Boid b
    FOR EACH BOID b
        b.velocity+=(Rule1(b)+(Rule2(b))+(Rule3(b)))
        b.position+=b.velocity
    END

```

## References
[^1]: https://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/ 
[^2]: https://vergenet.net/~conrad/boids/pseudocode.html
