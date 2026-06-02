import { useState } from "react";

export default function ContactForm() {
    // Společný stav pro všechna pole formuláře
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        message: ""
    });

    // Stav pro chybové hlášky
    const [errors, setErrors] = useState({
        name: "",
        email: "",
        message: ""
    });

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Univerzální handler pro změnu hodnot v inputech
    function handleChange(e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) {
        const { id, value } = e.target;
        
        setFormData(prev => ({
            ...prev,
            [id]: value
        }));

        // Promazání chyby, jakmile uživatel začne psát
        if (errors[id as keyof typeof errors]) {
            setErrors(prev => ({ ...prev, [id]: "" }));
        }
    }

    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();

        // Ořezání whitespace
        const cleanName = formData.name.trim();
        const cleanEmail = formData.email.trim();
        const cleanMessage = formData.message.trim();

        let valid = true;
        const newErrors = { name: "", email: "", message: "" };

        // 1. Validace Jména
        if (cleanName.length === 0) {
            newErrors.name = "Jméno je povinné.";
            valid = false;
        } else if (cleanName.length < 2) {
            newErrors.name = "Jméno musí mít alespoň 2 znaky.";
            valid = false;
        }

        // 2. Validace Emailu
        if (cleanEmail.length === 0) {
            newErrors.email = "Email je povinný.";
            valid = false;
        } else if (!emailRegex.test(cleanEmail)) {
            newErrors.email = "Zadejte platnou emailovou adresu.";
            valid = false;
        }

        // 3. Validace Zprávy
        if (cleanMessage.length === 0) {
            newErrors.message = "Zpráva je povinná.";
            valid = false;
        } else if (cleanMessage.length < 10) {
            newErrors.message = "Zpráva je příliš krátká (min. 10 znaků).";
            valid = false;
        }

        if (!valid) {
            setErrors(newErrors);
            return;
        }

        fetch(`http://localhost:8000/sent_email/${cleanEmail}/Kontaktni_formular`, {
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            
            return response.json();
        })
        .then(data => {
            console.log("Email sent successfully:", data);
        })
        .catch(error => {
            console.error("Error sending email:", error);
        });

        setFormData({ name: "", email: "", message: "" });
        setErrors({ name: "", email: "", message: "" });

    }

    return (
        <form onSubmit={handleSubmit} className="max-w-lg mx-auto bg-white p-8 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-6 text-center">Kontaktujte mě</h2>
            
            {/* Jméno */}
            <div className="mb-4">
                <label className="block text-gray-700 font-medium mb-2" htmlFor="name">
                    Jméno
                </label>
                <input 
                    type="text" 
                    id="name" 
                    value={formData.name}
                    onChange={handleChange} 
                    maxLength={50}
                    className={`w-full px-3 py-2 border ${errors.name ? 'border-red-500 focus:ring-red-500' : 'border-gray-300 focus:ring-blue-500'} rounded-md focus:outline-none focus:ring-2`} 
                    placeholder="Vaše jméno" 
                />
                {errors.name && <p className="text-red-500 text-sm mt-1">{errors.name}</p>}
            </div>

            {/* Email */}
            <div className="mb-4">
                <label className="block text-gray-700 font-medium mb-2" htmlFor="email">
                    Email
                </label>
                <input 
                    type="email" 
                    id="email" 
                    value={formData.email}
                    onChange={handleChange} 
                    maxLength={254}
                    className={`w-full px-3 py-2 border ${errors.email ? 'border-red-500 focus:ring-red-500' : 'border-gray-300 focus:ring-blue-500'} rounded-md focus:outline-none focus:ring-2`} 
                    placeholder="vaše emailová adresa" 
                />
                {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email}</p>}
            </div>

            {/* Zpráva */}
            <div className="mb-4">
                <label className="block text-gray-700 font-medium mb-2" htmlFor="message">
                    Zpráva
                </label>
                <textarea 
                    id="message" 
                    value={formData.message}
                    onChange={handleChange}
                    maxLength={1000}
                    className={`w-full px-3 py-2 border ${errors.message ? 'border-red-500 focus:ring-red-500' : 'border-gray-300 focus:ring-blue-500'} rounded-md focus:outline-none focus:ring-2`} 
                    rows={5} 
                    placeholder="Vaše zpráva" 
                ></textarea>
                {errors.message && <p className="text-red-500 text-sm mt-1">{errors.message}</p>}
            </div>

            <button 
                type="submit" 
                className="w-full bg-blue-600 text-white font-medium py-2 px-4 rounded-md hover:bg-blue-700 transition-colors"
            >
                Odeslat
            </button>
        </form>
    );
}