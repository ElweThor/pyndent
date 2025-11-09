#!/usr/bin/env python

#
# AI Memory Stats
# (C)2025 by Elwe Thor - Aria@DeepSeek 
# LICENSE: CC BY-NC-SA 4.0 (see LICENSE file for details)
#

import json
import re

def parse_memory_json(content):
    """Parsa il JSON anche con potenziali problemi di formato"""
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Fallback: regex parsing per estrarre i campi chiave
        entries = []
        entry_blocks = re.findall(r'\{[^{}]*?"id"[^{}]*?\}', content, re.DOTALL)
        
        for block in entry_blocks:
            entry = {}
            # Estrai id
            id_match = re.search(r'"id"\s*:\s*"([^"]*)"', block)
            if id_match:
                entry['id'] = id_match.group(1)
            
            # Estrai priority  
            prio_match = re.search(r'"priority"\s*:\s*"([^"]*)"', block)
            if prio_match:
                entry['priority'] = prio_match.group(1)
            else:
                entry['priority'] = 'medium'  # default
                
            # Estrai active
            active_match = re.search(r'"active"\s*:\s*(true|false)', block)
            if active_match:
                entry['active'] = active_match.group(1) == 'true'
            else:
                entry['active'] = True  # default
                
            # Estrai last_updated
            updated_match = re.search(r'"last_updated"\s*:\s*"([^"]*)"', block)
            entry['has_updates'] = bool(updated_match)
            
            entries.append(entry)
            
        return {'entries': entries}

def calculate_stats(data, content):
    entries = data['entries']
    total = len(entries)
    
    # Trova max_entries
    max_entries_match = re.search(r'"max_entries".*?"value":\s*(\d+)', content)
    max_entries = int(max_entries_match.group(1)) if max_entries_match else 100
    # Statistiche base
    active = [e for e in entries if e.get('active', True)]
    inactive = [e for e in entries if not e.get('active', True)]
    
    # Priorità attive
    active_prio = {
        'highest': len([e for e in active if e.get('priority') == 'highest']),
        'high': len([e for e in active if e.get('priority') == 'high']),
        'medium': len([e for e in active if e.get('priority') == 'medium']),
        'low': len([e for e in active if e.get('priority') == 'low'])
    }
    
    # Priorità inattive  
    inactive_prio = {
        'highest': len([e for e in inactive if e.get('priority') == 'highest']),
        'high': len([e for e in inactive if e.get('priority') == 'high']),
        'medium': len([e for e in inactive if e.get('priority') == 'medium']),
        'low': len([e for e in inactive if e.get('priority') == 'low'])
    }
    
    # Aggiornate vs Originali
    updated = len([e for e in entries if e.get('has_updates', False)])
    original = total - updated
    
    # Utilizzo e zona
	
    usage_pct = (total / max_entries) * 100
	if usage_pct <= 59:
		zone = "VERDE"
	elif usage_pct <= 79:
		zone = "ARANCIO" 
	elif usage_pct <= 99:
		zone = "ROSSA"
	else:
		zone = "NERA"	
    
    return {
        'total': total,
        'max_entries': max_entries,
        'active': len(active),
        'inactive': len(inactive),
        'active_prio': active_prio,
        'inactive_prio': inactive_prio,
        'updated': updated,
        'original': original,
        'usage_pct': usage_pct,
        'zone': zone,
        'entries': entries
    }

def generate_listing(entries):
    """Genera il listing con le 4 colonne richieste"""
    # Ordina per priorità (highest first)
    priority_order = {'highest': 0, 'high': 1, 'medium': 2, 'low': 3}
    sorted_entries = sorted(entries, key=lambda x: priority_order.get(x.get('priority', 'medium'), 4))
    
    listing = []
    current_prio = None
    p_counter = 0
    
    for i, entry in enumerate(sorted_entries, 1):
        prio = entry.get('priority', 'medium')
        
        if prio != current_prio:
            current_prio = prio
            p_counter = 1
        else:
            p_counter += 1
            
        status = "ACTIVE" if entry.get('active', True) else "inactive"
        
        listing.append({
            'N': i,
            'P': p_counter,
            'ID': entry.get('id', 'N/A'),
            'Prio': prio,
            'A': status
        })
    
    return listing

# MAIN
if __name__ == "__main__":
    try:
        with open('memory.json', 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = parse_memory_json(content)
        stats = calculate_stats(data, content)
        listing = generate_listing(data['entries'])
        
        # Output statistiche (SENZA EMOJI per compatibilità Windows)
        print("MEMORY STATS:")
        print(f"• Totali: {stats['total']} entries / {stats['max_entries']} max")
        print(f"• Attive: {stats['active']} ({stats['active']/stats['total']*100:.0f}%) vs Inattive: {stats['inactive']} ({stats['inactive']/stats['total']*100:.0f}%)")
        print(f"• Priorità attive: highest: {stats['active_prio']['highest']}, high: {stats['active_prio']['high']}, medium: {stats['active_prio']['medium']}, low: {stats['active_prio']['low']}")
        print(f"• Priorità inattive: highest: {stats['inactive_prio']['highest']}, high: {stats['inactive_prio']['high']}, medium: {stats['inactive_prio']['medium']}, low: {stats['inactive_prio']['low']}")
        print(f"• Aggiornate: {stats['updated']} ({stats['updated']/stats['total']*100:.0f}%) vs Originali: {stats['original']} ({stats['original']/stats['total']*100:.0f}%)")
        print(f"• Utilizzo: {stats['usage_pct']:.0f}% della capacità")
        
        # Zona senza emoji
        zone_text = stats['zone'].split(' ')[1]  # Prende solo "VERDE", "ARANCIO", etc.
        print(f"• Zona: {zone_text} ({stats['usage_pct']:.0f}%)")
        
        print("\nLISTING MEMORIE:")
        print(f"{'N':<3} {'P':<3} {'ID':<35} {'Prio':<8} {'A':<8}")
        print("-" * 60)
        for item in listing:
            print(f"{item['N']:<3} {item['P']:<3} {item['ID']:<35} {item['Prio']:<8} {item['A']:<8}")
            
    except Exception as e:
        print(f"ERRORE: {e}")
