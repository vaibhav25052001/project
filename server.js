import express from "express"
import dotenv from 'dotenv'
const app=express()

app.get('/',(req,res)=>{
    res.send('<h1>Welcome to Cutoff Prediction</h1>')
})

dotenv.config()
const PORT=process.env.PORT

//middleware
app.use(express.json())

app.listen(PORT,()=>{
    console.log(`Server running on ${PORT}`)
})