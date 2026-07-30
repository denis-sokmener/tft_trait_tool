import pulp
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from collections import Counter

# 1. SET 18 DATA (Units, Traits)
master_units = {
    "Akali": ["Inferno", "Adaptor", "Ravager"], "Azir": ["Blackthorn", "Executioner", "Summoner"],
    "Camile": ["Coven", "Ravager"], "Cinderling": ["Riftbeast", "Hunter"],
    "Karma": ["Blossom", "Spellweaver"], "Kobuko": ["Sprykin", "Brawler"],
    "Leona": ["Solar", "Defender"], "Ornn": ["Elderwood", "Defender"],
    "Pebbles": ["Riftbeast", "Invoker"], "Rakan": ["Fae", "Juggernaut", "Vanguard"],
    "Rek'Sai": ["Blackthorn", "Brawler"], "Varus": ["Inferno", "Rapidfire"],
    "Veigar": ["Blackthorn", "Sprykin", "Spellweaver"], "Xayah": ["Elderwood", "Fae", "Rapidfire"],
    "Yorick": ["Blossom", "Juggernaut", "Summoner"], "Alistar": ["Elderwood", "Brawler"],
    "Caitlyn": ["Coven", "Hunter"], "Elise": ["Coven", "Vanguard"],
    "Gromp": ["Riftbeast", "Adaptor"], "Kayle": ["Solar", "Rapidfire"],
    "Leblanc": ["Elderwood", "Spellweaver"], "Murkwolf": ["Riftbeast", "Ravager"],
    "Scuttlecrab": ["Riftbeast", "Juggernaut"], "Sejuani": ["Solar", "Juggernaut"],
    "Shen": ["Inferno", "Defender"], "Teemo": ["Sprykin", "Invoker"],
    "Warwick": ["Blackthorn", "Ravager"], "Yunara": ["Blossom", "Executioner"],
    "Cassiopeia": ["Coven", "Spellweaver"], "Diana": ["Lunar", "Ravager", "Vanguard"],
    "Fiddlestick": ["Flora Fatalis", "Defender", "Spellweaver"], "Hecarim": ["Elderwood", "Vanguard"],
    "Kha'Zix": ["Rival"], "Kog'Maw": ["Caustic", "Adaptor", "Invoker"],
    "Krug": ["Riftbeast", "Brawler"], "Mama Beak": ["Riftbeast", "Summoner", "Rapidfire"],
    "Master Yi": ["Blossom", "Adaptor"], "Rammus": ["Sprykin", "Defender"],
    "Rengar": ["Rival"], "Tristana": ["Fae", "Sprykin", "Hunter"],
    "Vi": ["Primal", "Juggernaut"], "Ahri": ["Blossom", "Spellweaver"],
    "Amumu": ["Inferno", "Juggernaut"], "Aphelios": ["Lunar", "Rapidfire"],
    "Brambleback": ["Riftbeast", "Ravager"], "Ezreal": ["Elderwood", "Executioner"],
    "Lillia": ["Fae", "Defender"], "Malphite": ["Blackthorn", "Monolith"],
    "Morgana": ["Coven", "Invoker"], "Nidalee": ["Primal", "Adaptor"],
    "Sentinel": ["Riftbeast", "Vanguard", "Invoker"], "Sett": ["Blossom", "Brawler"],
    "Sivir": ["Primal", "Hunter"], "Soraka": ["Flora Fatalis", "Executioner"],
    "Zyra": ["Thornmaiden", "Summoner"], "Alune": ["Attuned", "Lunar", "Spellweaver"],
    "Ashe": ["Blossom", "Hunter"], "Draven": ["Bounty Seeker"],
    "Elder Dragon": ["Apex Predator", "Riftbeast"], "Gnar": ["Elderwood", "Sprykin", "Brawler"],
    "Ivern": ["Greenfather"], "Kennen": ["Inferno", "Executioner"],
    "Lux (Blackthorn)": ["Blackthorn", "Avatar"], "Lux (Blossom)": ["Blossom", "Avatar"],
    "Lux (Coven)": ["Coven", "Avatar"], "Lux (Elderwood)": ["Elderwood", "Avatar"],
    "Lux (Fae)": ["Fae", "Avatar"], "Lux (Inferno)": ["Inferno", "Avatar"],
    "Lux (Moonbeam)": ["Lunar", "Avatar"], "Lux (Primal)": ["Primal", "Avatar"],
    "Lux (Sunbeam)": ["Solar", "Avatar"], "Maokai": ["Old Growth", "Juggernaut"],
    "Taric": ["Emerald Aspect", "Vanguard"]
}

# 2. UNIT COSTS (Gold)
unit_costs = {
    "Pebbles": 1, "Cinderling": 1, "Karma": 1, "Yorick": 1, "Leona": 1, "Ornn": 1, 
    "Rakan": 1, "Xayah": 1, "Varus": 1, "Veigar": 1, "Akali": 1, "Rek'Sai": 1, 
    "Kobuko": 1, "Camile": 1,
    "Scuttlecrab": 2, "Murkwolf": 2, "Gromp": 2, "Kayle": 2, "Sejuani": 2, "Leblanc": 2, 
    "Elise": 2, "Alistar": 2, "Yunara": 2, "Shen": 2, "Warwick": 2, "Teemo": 2, "Caitlyn": 2,
    "Krug": 3, "Mama Beak": 3, "Diana": 3, "Hecarim": 3, "Master Yi": 3, "Fiddlestick": 3, 
    "Rammus": 3, "Azir": 3, "Rengar": 3, "Kog'Maw": 3, "Tristana": 3, "Vi": 3, 
    "Cassiopeia": 3, "Kha'Zix": 3,
    "Brambleback": 4, "Sentinel": 4, "Amumu": 4, "Ahri": 4, "Sett": 4, "Ezreal": 4, 
    "Aphelios": 4, "Soraka": 4, "Lillia": 4, "Zyra": 4, "Morgana": 4, "Malphite": 4, 
    "Sivir": 4, "Nidalee": 4,
    "Lux (Blackthorn)": 5, "Lux (Blossom)": 5, "Lux (Coven)": 5, "Lux (Fae)": 5, 
    "Lux (Moonbeam)": 5, "Lux (Elderwood)": 5, "Lux (Inferno)": 5, "Lux (Primal)": 5, 
    "Lux (Sunbeam)": 5, "Taric": 5, "Ivern": 5, "Elder Dragon": 5, "Maokai": 5, 
    "Kennen": 5, "Gnar": 5, "Draven": 5, "Alune": 5, "Ashe": 5
}

# 3. TRAIT ACTIVATION THRESHOLDS
trait_thresholds = {
    "Inferno": 2, "Adaptor": 2, "Ravager": 2, "Blackthorn": 2,
    "Executioner": 2, "Summoner": 2, "Coven": 3, "Riftbeast": 3,
    "Hunter": 2, "Blossom": 3, "Spellweaver": 2, "Sprykin": 3,
    "Brawler": 3, "Solar": 3, "Defender": 2, "Elderwood": 3,
    "Invoker": 2, "Fae": 2, "Juggernaut": 2, "Vanguard": 2,
    "Rapidfire": 2, "Lunar": 2, "Flora Fatalis": 1, "Rival": 1,
    "Caustic": 1, "Primal": 2, "Monolith": 1, "Thornmaiden": 1,
    "Attuned": 1, "Bounty Seeker": 1, "Apex Predator": 1,
    "Greenfather": 1, "Avatar": 1, "Old Growth": 1, "Emerald Aspect": 1
}

# 4. IGNORED TRAITS (Non-Unique / Excluded from score)
ignored_traits = [
    "Rival", "Caustic", "Monolith", "Thornmaiden", "Attuned",
    "Bounty Seeker", "Apex Predator", "Greenfather", "Avatar",
    "Old Growth", "Emerald Aspect"
]

def run_algorithm(board_size, required_traits, include_high_costs, emblem_trait, target_trait_count=None):
    # 1. Filter the unit pool based on cost settings
    if include_high_costs:
        active_units = master_units.copy()
    else:
        active_units = {u: traits for u, traits in master_units.items() if unit_costs[u] <= 3}
        
    if not active_units:
        return "Error: No units available in the pool."

    # 2. Map traits to their corresponding units
    trait_to_units = {trait: [] for trait in trait_thresholds}
    trait_unit_multiplier = {trait: {} for trait in trait_thresholds}
    
    for u, u_traits in active_units.items():
        for trait in u_traits:
            if trait in trait_to_units:
                trait_to_units[trait].append(u)
                # Double count Lux variants (except Avatar)
                trait_unit_multiplier[trait][u] = 2 if ("Lux" in u and trait != "Avatar") else 1

    valid_trait_keys = [t for t in trait_thresholds if t not in ignored_traits]
    max_trait_score = None

    # PHASE 1: FIND MAXIMUM TRAITS IF NO TARGET IS SPECIFIED
    if target_trait_count is None:
        prob_max = pulp.LpProblem("Maximize_Traits", pulp.LpMaximize)
        u_vars = {u: pulp.LpVariable(f"u_{u.replace(' ', '_').replace('(', '').replace(')', '')}", cat="Binary") for u in active_units}
        t_vars = {t: pulp.LpVariable(f"t_{t.replace(' ', '_')}", cat="Binary") for t in trait_thresholds}

        # Constraint: Total units must equal board size
        prob_max += pulp.lpSum(u_vars.values()) == board_size

        for trait, threshold in trait_thresholds.items():
            units_here = trait_to_units[trait]
            emblem_bonus = 1 if trait == emblem_trait else 0
            
            if units_here or emblem_bonus > 0:
                prob_max += pulp.lpSum(trait_unit_multiplier[trait][u] * u_vars[u] for u in units_here) + emblem_bonus >= threshold * t_vars[trait]
            else:
                prob_max += t_vars[trait] == 0

        # Constraint: Required traits must be active
        for req_trait in required_traits:
            if req_trait in t_vars:
                prob_max += t_vars[req_trait] == 1

        prob_max += pulp.lpSum(t_vars[t] for t in valid_trait_keys)
        prob_max.solve(pulp.PULP_CBC_CMD(msg=False))

        if prob_max.status != pulp.LpStatusOptimal:
            return "ERROR: Could not find any valid board satisfying these conditions.\nCheck if your required traits fit within the board size."
        
        max_trait_score = int(pulp.value(prob_max.objective))

    # PHASE 2: FIND THE CHEAPEST BOARDS THAT ACHIEVE THE TARGET SCORE
    prob_min = pulp.LpProblem("Minimize_Cost", pulp.LpMinimize)
    u_vars_m = {u: pulp.LpVariable(f"um_{u.replace(' ', '_').replace('(', '').replace(')', '')}", cat="Binary") for u in active_units}
    t_vars_m = {t: pulp.LpVariable(f"tm_{t.replace(' ', '_')}", cat="Binary") for t in trait_thresholds}

    prob_min += pulp.lpSum(u_vars_m.values()) == board_size

    for trait, threshold in trait_thresholds.items():
        units_here = trait_to_units[trait]
        emblem_bonus = 1 if trait == emblem_trait else 0
        
        if units_here or emblem_bonus > 0:
            prob_min += pulp.lpSum(trait_unit_multiplier[trait][u] * u_vars_m[u] for u in units_here) + emblem_bonus >= threshold * t_vars_m[trait]
        else:
            prob_min += t_vars_m[trait] == 0

    for req_trait in required_traits:
        if req_trait in t_vars_m:
            prob_min += t_vars_m[req_trait] == 1

    # Lock to the target score
    if target_trait_count is not None:
        prob_min += pulp.lpSum(t_vars_m[t] for t in valid_trait_keys) >= target_trait_count
    else:
        prob_min += pulp.lpSum(t_vars_m[t] for t in valid_trait_keys) == max_trait_score

    # Objective: Minimize total gold cost
    prob_min += pulp.lpSum(u_vars_m[u] * unit_costs[u] for u in active_units)

    found_boards = []
    MAX_BOARDS_TO_SEARCH = 20 # Number of boards to search for statistics pool

    # Loop to find alternative boards
    while len(found_boards) < MAX_BOARDS_TO_SEARCH:
        prob_min.solve(pulp.PULP_CBC_CMD(msg=False))
        if prob_min.status != pulp.LpStatusOptimal:
            break
            
        selected_units = [u for u in u_vars_m if u_vars_m[u].varValue is not None and u_vars_m[u].varValue > 0.5]
        active_traits = [t for t in t_vars_m if t_vars_m[t].varValue is not None and t_vars_m[t].varValue > 0.5 and t not in ignored_traits]
        total_board_cost = int(sum(unit_costs[u] for u in selected_units))
        
        found_boards.append((selected_units, active_traits, total_board_cost))
        
        # Prevent finding this exact board again
        prob_min += pulp.lpSum(u_vars_m[u] for u in selected_units) <= board_size - 1

    # Format the output string
    output_str = f"--- RESULTS FOR BOARD SIZE {board_size} ---\n"
    output_str += f"Required Traits: {', '.join(required_traits) if required_traits else 'None'}\n"
    output_str += f"Emblem Added: {emblem_trait if emblem_trait else 'None'}\n"
    
    if target_trait_count is not None:
        output_str += f"Target Minimum Traits: {target_trait_count}\n\n"
    else:
        output_str += f"Max Main Traits Reached: {max_trait_score}\n\n"

    if not found_boards:
        output_str += "No valid boards found. Try lowering your target count or increasing board size."
    else:
        # CALCULATE STATISTICS (Based on all optimal boards found)
        all_units = []
        for board, _, _ in found_boards:
            all_units.extend(board)
            
        total_found = len(found_boards)
        unit_counts = Counter(all_units)
        
        output_str += f"--- UNIT FREQUENCY (Based on {total_found} optimal boards) ---\n"
        # Display the top 10 most frequently used units
        for unit, count in unit_counts.most_common(10):
            percentage = (count / total_found) * 100
            output_str += f"- {unit}: {percentage:.1f}%\n"
        output_str += "\n--- TOP 3 CHEAPEST EXAMPLE BOARDS ---\n\n"

        # Print only the first 3 cheapest examples
        for i, (board, traits, cost) in enumerate(found_boards[:3], 1):
            output_str += f"Example Board #{i} (Total Cost: {cost} Gold)\n"
            output_str += f"Units: {', '.join(board)}\n"
            output_str += f"Total Active Main Traits: {len(traits)}\n\n"
            
    return output_str

# GUI CODE
class TFTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TFT Board Optimizer")
        self.root.geometry("650x750")
        self.root.configure(padx=20, pady=20)

        ttk.Label(root, text="Board Size (Units):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.board_size_entry = ttk.Entry(root)
        self.board_size_entry.insert(0, "8")
        self.board_size_entry.grid(row=0, column=1, sticky=tk.EW, pady=5)

        ttk.Label(root, text="Required Traits (Comma separated):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.traits_entry = ttk.Entry(root)
        self.traits_entry.grid(row=1, column=1, sticky=tk.EW, pady=5)

        ttk.Label(root, text="+1 Emblem (Optional):").grid(row=2, column=0, sticky=tk.W, pady=5)
        trait_list = ["None"] + sorted(list(trait_thresholds.keys()))
        self.emblem_combo = ttk.Combobox(root, values=trait_list, state="readonly")
        self.emblem_combo.current(0)
        self.emblem_combo.grid(row=2, column=1, sticky=tk.EW, pady=5)

        ttk.Label(root, text="Minimum Trait Count (Optional):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.target_count_entry = ttk.Entry(root)
        self.target_count_entry.grid(row=3, column=1, sticky=tk.EW, pady=5)

        self.include_high_costs_var = tk.BooleanVar(value=True)
        self.cost_check = ttk.Checkbutton(root, text="Include 4 and 5 Cost Units", variable=self.include_high_costs_var)
        self.cost_check.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=10)

        self.calc_btn = ttk.Button(root, text="Calculate Best Boards", command=self.calculate)
        self.calc_btn.grid(row=5, column=0, columnspan=2, pady=15, sticky=tk.EW)

        ttk.Label(root, text="Results:").grid(row=6, column=0, sticky=tk.W)
        self.result_text = scrolledtext.ScrolledText(root, height=20, width=65)
        self.result_text.grid(row=7, column=0, columnspan=2, pady=5, sticky=tk.NSEW)

        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(7, weight=1)

    def calculate(self):
        try:
            b_size = int(self.board_size_entry.get().strip())
            if b_size <= 0:
                messagebox.showerror("Error", "Board size must be greater than 0.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for Board Size.")
            return

        req_traits_raw = self.traits_entry.get().strip()
        parsed_traits = []
        if req_traits_raw:
            raw_list = [t.strip().title() for t in req_traits_raw.split(",")]
            for t in raw_list:
                if t in trait_thresholds:
                    parsed_traits.append(t)
                else:
                    messagebox.showwarning("Warning", f"Trait '{t}' not found in database. It will be ignored.")

        target_val = self.target_count_entry.get().strip()
        target_count = None
        if target_val:
            try:
                target_count = int(target_val)
                if target_count <= 0:
                    messagebox.showerror("Error", "Target trait count must be greater than 0.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer for Target Trait Count.")
                return

        include_high = self.include_high_costs_var.get()
        emb_val = self.emblem_combo.get()
        emblem = emb_val if emb_val != "None" else None

        self.calc_btn.config(text="Calculating...", state=tk.DISABLED)
        self.root.update()

        result_str = run_algorithm(b_size, parsed_traits, include_high, emblem, target_count)
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_str)
        
        self.calc_btn.config(text="Calculate Best Boards", state=tk.NORMAL)

if __name__ == "__main__":
    app_root = tk.Tk()
    app = TFTApp(app_root)
    app_root.mainloop()
