const workExperience = [
    {
        id: 1,
        period: "2023 - dosud",
        position: "MES Consultant",
        company: "Hyundai AutoEver Europe",
        description: "Správa hardware a software ve výrobě, implementace a údržba MES (Manufacturing Execution System) systémů pro optimalizaci výrobních procesů.",
        skills: ["MES", "Hardware", "Software", ".NET"],
        color: "blue",
        logo: "https://media.licdn.com/dms/image/v2/D560BAQFctTvIDtEcSA/company-logo_200_200/B56Z2VSsHNGoAI-/0/1776326198308/hyundai_autoever_europe_czech_republik_logo?e=1781740800&v=beta&t=PkVsBtJhQTW5r2fhckS3fg3gBL5BPWnj1m4umFnwUFI",
        isActive: true
    },
    {
        id: 2,
        period: "2022 - 2025",
        position: "Lektor",
        company: "Step It Academy - Ostrava",
        description: "Výuka programování a IT technologií, příprava výukových materiálů a vedení praktických workshopů pro studenty různých úrovní.",
        skills: ["Vzdělávání", "Programování", "IT", "Python", "HTML", "JavaScript"],
        color: "green",
        logo: "https://media.licdn.com/dms/image/v2/C510BAQEyfKQsdWriRg/company-logo_200_200/company-logo_200_200/0/1631375274397?e=1781740800&v=beta&t=eJ_BwGObJsO3YMPDYoAiIjnwLyWVILcxHYsA_0b7bZs",
        isActive: false
    },
    {
        id: 3,
        period: "2021 - 2023",
        position: "Webový administrátor",
        company: "Klub DIXI Havířov",
        description: "Kompletní správa a tvorba webových stránek klubu, včetně design, development, SEO optimalizace a pravidelných aktualizací obsahu.",
        skills: ["Web Development", "Design", "SEO"],
        color: "purple",
        logo: "./works-logo/Logo-DIXI-JPG.jpg",
        isActive: false
    }
];

const getColorClasses = (color: string) => {
    const colorMap = {
        blue: {
            dot: "bg-blue-600",
            time: "text-blue-600 dark:text-blue-400",
            skills: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300"
        },
        green: {
            dot: "bg-green-600",
            time: "text-green-600 dark:text-green-400",
            skills: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300"
        },
        purple: {
            dot: "bg-purple-600",
            time: "text-purple-600 dark:text-purple-400",
            skills: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-300"
        }
    };
    return colorMap[color as keyof typeof colorMap] || colorMap.blue;
};

const getSkillColor = (skill: string, index: number) => {
    const skillColors = [
        "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300",
        "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300", 
        "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-300",
        "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300",
        "bg-pink-100 text-pink-800 dark:bg-pink-900 dark:text-pink-300",
        "bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-300"
    ];
    return skillColors[index % skillColors.length];
};

export default function Timeline() {
    return (
        <section className="p-6 max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold mb-8 text-center bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                Pracovní zkušenosti
            </h2>
            <ol className="relative border-s-2 border-gray-200 dark:border-gray-700">
                {workExperience.map((job, index) => {
                    const colors = getColorClasses(job.color);
                    const isLast = index === workExperience.length - 1;
                    
                    return (
                        <li key={job.id} className={`${isLast ? 'mb-0' : 'mb-12'} ms-6`}>
                            <div className={`absolute w-4 h-4 ${colors.dot} rounded-full mt-1.5 -start-2 border-2 border-white dark:border-gray-900 shadow-lg`}></div>
                            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md border border-gray-200 dark:border-gray-700">
                                <time className={`mb-2 text-sm font-medium ${colors.time} uppercase tracking-wide`}>
                                    {job.period}
                                </time>
                                <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
                                    {job.position}
                                </h3>
                                <div className="text-lg font-medium text-gray-700 dark:text-gray-300 mb-3 flex items-center gap-2">
                                    <img src={job.logo} alt={`${job.company} logo`} className="w-6 h-6 rounded-full" />
                                    {job.company}
                                </div>
                                <p className="text-base text-gray-600 dark:text-gray-400 mb-4">
                                    {job.description}
                                </p>
                                <div className="flex flex-wrap gap-2">
                                    {job.skills.map((skill, skillIndex) => (
                                        <span 
                                            key={skillIndex} 
                                            className={`px-3 py-1 text-xs font-medium rounded-full ${getSkillColor(skill, skillIndex)}`}
                                        >
                                            {skill}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        </li>
                    );
                })}
            </ol>
        </section>
    );
}