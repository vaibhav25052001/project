import mongoose, { mongo } from "mongoose"
const userSchema=new mongoose.Schema({
    category:{
        type:String,
        required:true,
        trim:true
    },
    gender:{
        type:String,
        required:true,
    },
    opening_rank:{
        type:String,
        required:true
    },
    closing_rank:{
        type:String,
        required:true
    },
    quota:{
        type:String,
        required:true
    },
    round_no:{
        type:String,
        required:true
    }
},{timestamps:true})
export default mongoose.model('users',userSchema)