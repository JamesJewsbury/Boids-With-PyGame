# Boids With PyGame
![Photo by <a href="https://unsplash.com/@tumbao1949?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">James Wainscoat</a> on <a href="https://unsplash.com/photos/a-large-flock-of-birds-flying-over-a-field-b7MZ6iGIoSI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      ]("./Assets/Images/Flock of Birds.jpg")
> Photo by <a href="https://unsplash.com/@tumbao1949?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">James Wainscoat</a> on <a href="https://unsplash.com/photos/a-large-flock-of-birds-flying-over-a-field-b7MZ6iGIoSI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
    
## Outline
In this project, I will be using basic Python libraries and PyGame to replicate 'boids' as detailed by Craig Reynolds in his 1987 publication "Flocks, Herds, and Schools: A Distributed Behaviour Model"[^1].

In short, Reynolds showed that the complex and fluid movements exhibited by flocks of birds or schools of fish, can be attributed to simple decisions being made by each individual being. Reynolds created 3 simple rules that controlled these agents:
1. **Collision Avoidance**: Just as a bird would not want to collide with it's flock-mate, neither would these boids.
2. **Velocity Matching**: Boids try to "keep-up" with one another (speed) and have a similar direction. 
3. **Flock Centering**: Boids aim to stay near the centre of the N other nearby boids.










## References
[^1] https://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/ 